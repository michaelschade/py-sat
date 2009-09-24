QUESTION_URL    = 'http://apps.collegeboard.com/qotd/question.do?src=O&questionId='
MAX_ID          = 1208

subject_set     = []

def _retrieve_subject(qid):
    from urllib2 import Request, urlopen
    headers = {
        'User-Agent': 'Question Meta Grabber/0.5b (Michael Schade)',
    }
    questionPage = urlopen(Request('%s%s' % (QUESTION_URL, qid), headers=headers))
    from lxml import html
    questionPage = html.fromstring(questionPage.read())
    try:
        subject = questionPage.get_element_by_id('section').getparent().text_content()[9:]
    except KeyError:
        return ''
    return subject

def main():
    for qid in range(MAX_ID):
        subject = _retrieve_subject(qid)
        subject_set.append(subject)
        print "Retrieved subject '%s' (question %d of %d)." % (subject, qid+1, MAX_ID-1)
    subjects = open('subjects.txt', 'w')
    subjects.writelines(['%s\n' % subject for subject in subject_set])
    subjects.close()

if __name__ == '__main__':
    main()

# EOF

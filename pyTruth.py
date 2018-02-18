import optparse
import urllib



def performNLP():
    ###Perform NLP and return set of statements to fact check
    a=1

def factCheck():
    ###Take returned NLP statements and check against a list of configured sources
    a=1

def computeTruth():
    performNLP()
    factCheck()



def parseUrl(urlToParse):
    ###Code to Parse webpage
    ### Code to extract only content (excluding Ads and irrelevant content)
    a=1



def main():
    opID = optparse.OptionParser("usage%prog -u <url?")
    opID.add_option("-u", dest='url', type='string', help='specify URL')
    (options, args) = opID.parse_args()
    if (options.url == None):
        print opID.usage
        exit(0)
    else:
        urlToParse = options.url
    parseUrl(urlToParse)
    #Start with the following URL
    ###http: // time.com / 4912055 / donald - trump - phoenix - arizona - transcript /

if __name__ == '__main__':
    main()
    # Path / Users / harishvk / PycharmProjects / po

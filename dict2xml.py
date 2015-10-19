#   Python Dictionary to XML converter
#   Written by github.com/Pilfer
#   @CodesStuff
class dict2xml:
    def __init__(self, debug = False):
        self.debug = debug
        if self.debug:
            print "json2xml class has been loaded"

    def genXML(self,xmldict):
        tag = xmldict['tag']
        attrs = []
        kidstack = []
        for attr in xmldict['attributes']:
            attrs.append(str("%s=\"%s\"") % (attr['name'],attr['value']))
        if xmldict['children'] != None:
            for child in xmldict['children']:
                tmp = self.genXML(child)
                kidstack.append(tmp)
            if(len(kidstack) == 0):
                children = None
            else:
                children = "\n\t".join(kidstack)
        else:
            children = None
        xmlout = str("<%s %s>%s</%s>") % (tag, ' '.join(attrs), children if children != None else '',tag)
        return xmlout

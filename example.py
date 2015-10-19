from dict2xml import dict2xml

if __name__ == "__main__":

    dictToConvert = {
        "tag" : "authentication",
        "attributes" : [
            {
                "name" : "realm",
                "value" : "some-realm-here"
            },
            {
                "name" : "role",
                "value" : "administrator"
            }
        ],
        "children" : [{
            "tag" : "credentials",
            "attributes" : [
                {
                    "name" : "username",
                    "value" : "pilfer"
                },
                {
                    "name" : "email",
                    "value" : "pilfer@git.hub"
                },
                {
                    "name" : "token",
                    "value" : "1337h4x4l1f3=="
                }
            ],
            "children" : None
        }]

    }



    d2x = dict2xml(False) #False for no debug, True for debug
    print d2x.genXML(dictToConvert) #<authentication realm="some-realm-here" role="administrator"><credentials username="pilfer" email="pilfer@git.hub" token="1337h4x4l1f3=="></credentials></authentication>

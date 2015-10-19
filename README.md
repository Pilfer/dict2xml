# dict2xml
Really simple Python dictionary to XML converter.
Put children as an object array or None inside the parent object - it'll call itself again and make it xml-y.
There is no indent/pretty-print support because I hate XML and want it to die.

## Example...
```python
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
  print d2x.genXML(dictToConvert) 
  # Output:
  # <authentication realm="some-realm-here" role="administrator"><credentials username="pilfer" email="pilfer@git.hub" token="1337h4x4l1f3=="></credentials></authentication>

```

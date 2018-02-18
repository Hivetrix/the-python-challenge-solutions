# Python Challenge - Level 13

- Link: http://www.pythonchallenge.com/pc/return/disproportional.html
- Username: **huge**
- Password: **file**

## Problem

![](src/level_13/disprop.jpg)



> phone that evil 

Key 5 is clickable,

```xml
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value>
            <int>105</int>
          </value>
        </member>
        <member>
          <name>faultString</name>
          <value>
            <string>
              XML error: Invalid document end at line 1, column 1
            </string>
          </value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>
```

## Solution

We can use ``xmlrpc`` module to talk to it:

```python
>>> import xmlrpc.client
>>> conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
>>> conn
<ServerProxy for www.pythonchallenge.com/pc/phonebook.php>
>>> conn.system.listMethods()
['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
```

``phone`` seems to be the method we should call. Get more info on how to use it:

```python
>>> conn.system.methodHelp("phone")
'Returns the phone of a person'
>>> conn.system.methodSignature("phone")
[['string', 'string']]
```

So it takes a string and returns a string, the input should be the name and the output should be the number:

```python
>>> conn.phone("Bert")
'555-ITALY'
```

If you do not know, ``555`` basically means "fake phone numbers" in US... The key is "**italy**".

### Put Everything Together

```python
import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.phone("Bert"))
```

## Next Level

http://www.pythonchallenge.com/pc/return/italy.html

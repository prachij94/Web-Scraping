

# Web Scraping


> Web scraping is a computer software technique of extracting information from websites. This technique mostly focuses on the transformation of unstructured data (HTML format) on the web into structured data (database or spreadsheet).

We will use Python for scraping because of its ease .It has a library known as **‘Beautiful Soup’** which assists this task.



*There is no universal solution for web scraping because the way data is stored on each website is usually specific to that site. In fact, if you want to scrape the data, you need to understand the website’s structure.*


## Getting Started

Explore the website you want to scrape.
Accordingly, plan your code to pick the attribute values from the corresponding html elements in the website page which will provide you the information you wish to extract out.


## Prerequisites

- Overview of HTML   ( See a detailed [technical document](https://docs.google.com/document/d/1oIlcQyOpI1HMYOcan4MxPmSxGh2vj6cRAOJFQoYZGMw/edit?usp=sharing) taking a website as an example )
- Basic Understanding in application of Python concepts  (The [python implementation](Spareshub/spareshubbrands.py) of the website taken up in the above HTML document can help in getting acquainted)
- Use of automation tools like Selenium


## Example

Let us take up the example of the url http://www.industrybuying.com/office-chairs-ib-basics-OFF.OFF.41380990/ and get the details like Product Name and Product Specifications from there.



lxml is an extensive library written for parsing XML and HTML documents very quickly, even handling messed up tags in the process.
requests module provides the functionality of getting responses by hitting url's and has improved speed and readability

```
from lxml import html  
import requests
```



Store the url into a variable
```
url  = 'http://www.industrybuying.com/office-chairs-ib-basics-OFF.OFF.41380990/'
```



Specifying which user-agents to be used according to the browser when url requests are being made
```
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
```


To request a response from the server, there are mainly two types of methods, namely , GET and POST.
GET : to request data from the server & POST : to submit data to be processed to the server.
 
So we are using here the GET method along with the above headers.
Requests ignore verifying the SSL certificate if you set verify to False
```
page = requests.get(url,headers = headers,verify=False)
```


Decrypyting the html response received as a text formatted string having html tages,etc.
```
page_response = page.text
```


Creating a parser from the html content in the page, so as to use it further for extracting required sections' information
```
parser = html.fromstring(page.content)
```

Pass the xpath of the required product name html section(using the html inspector) into the parser.xpath() and store it into a variable productname.
Then, processing the text content of the above variable by removing leading and trailing spaces using strip()
```
productname = parser.xpath('//*[@id="main"]/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/span/h1')
name = productname[0].text_content().strip()
```

Pass the xpath of the required product specifications html section(using the html inspector) into the parser.xpath() and store it into a variable productspecs.
Then, processing the text content of the above variable by removing leading and trailing spaces using strip() and separating using newline character to create list of separated elements
```
productspecs = parser.xpath('//*[@id="productSpecifications"]/table')
    
a = productspecs[0].text_content().strip().split('\n')
```


Removing the leading and trailing spaces from each of the elements in the above list, removing out the blank elements using filter() and removing the unrequired header element i.e. the 0th element a[0]
```
a = [x.strip(' ') for x in a]
a= list(filter(None,a))
a.remove(a[0])
```


Finally creating the desired format of Product Specifications i.e Key:Value, by using a Python dictionary using dict() where we are zipping together the odd positioned elements with their respective even postioned values in the above aggregated list i.e. a
```
data = dict(zip(a[::2], a[1::2]))
```
Then, the extracted data can be exported into a csv file using the 'pandas' library in Python.

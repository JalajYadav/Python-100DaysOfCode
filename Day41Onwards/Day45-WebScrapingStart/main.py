from bs4 import BeautifulSoup
# import lxml
with open("./website.html",mode="r",encoding='utf-8') as file:
    data = file.read()


soup = BeautifulSoup(data,'html.parser')
# print(soup.title)           # to print the whole tag with the opening content and closing
# print(soup.title.name)      # to print the name of the tag specified
# print(soup.title.string)    # to print the content of the title tag
# print(soup.prettify())      # to print in indented manner
# print(soup.h3)              # to get the first h3 tag from the html file


# ----------------to find all the tag with a specific tagName---------------#
all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())    # to print the content of the tag
    print(tag.get("href"))  # to print the content of href attribute

# ----------------to find a unique tag----------------------#

h1_with_id_name = soup.find(name="h1",id="name")
print(h1_with_id_name)
print(h1_with_id_name.get("id"))

h3_with_class_heading = soup.find(name="h3",class_="heading")
print(h3_with_class_heading)
print(h3_with_class_heading.getText())

# ----------------to select element using selector--------------#

anchor_tag_inside_p_tag = soup.select_one(selector="p a")
print(anchor_tag_inside_p_tag)

tag_with_id_nama = soup.select_one(selector="#name")
print(tag_with_id_nama)

all_elements_with_class_heading = soup.select(selector=".heading")
print(all_elements_with_class_heading)



import os

old = "jashezan"
new = "shez4n"

# com_old_data = r"""\"/components"""
# com_new_data = r"""\"./components"""

# css_old_data = r"""\"/css"""
# css_new_data = r"""\"./css"""

# font_old_data = r"""\"/fonts"""
# font_new_data = r"""\"./fonts"""

# img_old_data = r"""\"/img"""
# img_new_data = r"""\"./img"""

# js_old_data = r"""\"/js"""
# js_old_data2 = r""";/js"""
# js_new_data = r""";./js"""

# print(old_data)
# print(new_data)

dr = "/home/shezan/Downloads/New/preview"

for root, dirs, files in os.walk(dr):
    for f in files:
    	if f[-4:] == "html":
            file_full_path = root + os.sep + f
            f = open(file_full_path,'r')
            filedata = f.read()
            f.close()

            # newdata = filedata.replace(com_old_data,com_new_data)
            # newdata = filedata.replace(css_old_data,css_new_data)
            # newdata = filedata.replace(font_old_data,font_new_data)
            # newdata = filedata.replace(img_old_data,img_new_data)
            # newdata = filedata.replace(js_old_data,js_new_data)
            # newdata = filedata.replace(js_old_data2,js_new_data)
            newdata = filedata.replace(old,new)

            f = open(file_full_path,'w')
            f.write(newdata)
            f.close()
            print(file_full_path)
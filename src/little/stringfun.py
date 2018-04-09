def stringfun():
    page = '''<div id="top_bin"> <div id="top_content" class="width960">
       <div class="udacity float-left"> <a href="https://classroom.udacity.com/courses/cs101/lessons/48299949/concepts/484805740923">'''

    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    print page[start_quote+1:end_quote]

    x = 3.84159

    y = str(x+0.5)
    print(y[:y.find('.')])

    print(10/4.0)
    print(10/4)
    print(10.0/5)
    print(10*1.0/4)
    print(10/5)
    print(10/50)
stringfun()

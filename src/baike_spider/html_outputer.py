# -*- coding: utf-8 -*-
# @Time    : 6/4/2018 2:09 PM
# @Author  : Jacklyn


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w',encoding='utf-8')
        fout.write('''<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
  </head>
 <body>
  <nav class="navbar navbar-default navbar-static-top"> 
   <div class="container"> 
    <div class="navbar-header"> 
     <button class="navbar-toggle collapsed" aria-expanded="false" aria-controls="navbar" type="button" data-toggle="collapse" data-target="#navbar"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> 
     <a class="navbar-brand" href="#">Project name</a> 
    </div> 
    <div class="collapse navbar-collapse" id="navbar"> 
     <ul class="nav navbar-nav"> 
      <li class="active"><a href="#">Home</a></li> 
      <li><a href="#about">About</a></li> 
      <li><a href="#contact">Contact</a></li> 
      <li class="dropdown"> <a class="dropdown-toggle" role="button" aria-expanded="false" aria-haspopup="true" href="#" data-toggle="dropdown">Dropdown <span class="caret"></span></a> 
       <ul class="dropdown-menu"> 
        <li><a href="#">Action</a></li> 
        <li><a href="#">Another action</a></li> 
        <li><a href="#">Something else here</a></li> 
        <li class="divider" role="separator"></li> 
        <li class="dropdown-header">Nav header</li> 
        <li><a href="#">Separated link</a></li> 
        <li><a href="#">One more separated link</a></li> 
       </ul> </li> 
     </ul> 
    </div>
    <!--/.nav-collapse --> 
   </div> 
  </nav> 
  <!-- Begin page content --> 
  <div class="container"> 
   <div class="page-header"> 
    <h1>baike_spider</h1> 
    <div class="table-responsive"> 
     <table class="table table-condensed table-striped"> 
      <tbody>
       <tr> 
        <th>title</th>
        <th>summary</th>
        <th>url</th> 
       </tr> 
        ''')

        for data in self.datas:
            fout.write("       <tr>\n")
            fout.write("       <td>%s</td>\n" % data['title'])
            fout.write("       <td>%s</td>\n" % data['summary'])
            fout.write("       <td>%s</td>\n" % data['url'])
            fout.write("       </tr>\n")

        fout.write('''
      </tbody>
     </table>
    </div> 
    <footer class="footer"> 
     <div class="container"> 
      <p class="text-muted">Place sticky footer content here.</p> 
     </div> 
    </footer> 
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) --> 
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script> 
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 --> 
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>   
   </div>
  </div>
 </body>
</html>''')

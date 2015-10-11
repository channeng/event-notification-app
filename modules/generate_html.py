import datetime
import time
import sys
import os

class Generate_html(object):
  def __init__(self,search,free_paid,category,period,city):
    self.email_title = "Upcoming Events in " + city
    self.subtitle = free_paid+ ' events ' + period +': ' + category
    self.table_title = "Free events"
    self.header_list = ['Event','Name','Description','Start','To','Link']
    self.search_results = []
    for i in search:
      # print i
      self.search_results += [['<img src="'+i.get("logo","")+'" width="192">',i["event_name"],i["description"],i["start"],i["end"],i["url"]]]
    
  # Get Data
  reload(sys)
  sys.setdefaultencoding('utf8')
  
  
  # Generate HTML functions
  def generate_header(self):
    return '''
    <h4 style="display: block;font-family: 'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;font-size: 16px;font-style: normal;font-weight: bold;line-height: 100%;letter-spacing: normal;margin-top: 0;margin-right: 0;margin-bottom: 0;margin-left: 0;text-align: left;color: #4A4A4A !important;">'''+self.subtitle+'''</h4>
    '''

  def generate_summary(self):
    total_all = len(self.search_results)
    return '''
    <p>Total: '''+str(total_all)+''' events found on Eventbrite</p>
    '''

  def generate_table_headers(self):
    headers_html = "<tr>"
    for i in self.header_list:
      headers_html += '<th style="font-family:Arial, sans-serif;font-size:14px;font-weight:bold;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;background-color:#bbdaff;color:#000000;text-align:center">'+str(i)+'</th>'
    headers_html += "</tr>"
    return headers_html

  def generate_table_row(self,row_list):
    row_html = "<tr>"
    for i in range(len(row_list)-1):
      row_html += '<td style="font-family:Arial, sans-serif;font-size:14px;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;background-color:#f8fbff;text-align:center;min-width:80px;">'+str(row_list[i])+'</td>'
    for i in range(1,2):
      row_html += '<td style="font-family:Arial, sans-serif;font-size:14px;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;background-color:#f8fbff;text-align:center"><a href="'+str(row_list[-i])+'" target="_blank" style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; color: #0099ED; font-weight: bold; text-decoration: none;">Link</a></td>'
    row_html += "</tr>"
    return row_html

  def generate_table_rows(self):
    table_rows_html = ""
    for row_list in self.search_results:
      table_rows_html += self.generate_table_row(row_list)
    return table_rows_html

  def generate_table(self):
    if len(self.search_results) == 0:
      pass
    else:
      return '<table style="border-collapse:collapse;border-spacing:0;">'+ self.generate_table_headers() + self.generate_table_rows() +'</table>' # removed table title before <table style> - <p style="font-weight: bold;">'+table_title+'</p>

  def generate_html(self):
    if len(self.search_results) == 0:
      print 'Events Report - NO search results found ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      exit()
    else:
      return '''<!DOCTYPE html>
      <html>
      <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
        <title>Nitrous</title>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans:400,700,300" rel="stylesheet" type="text/css">
        <style type="text/css">
            #outlook a{
                  padding:0;
              }
              .ReadMsgBody{
                  width:100%;
              }
              .ExternalClass{
                  width:100%;
              }
              .ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{
                  line-height:100%;
              }
              body,table,td,p,a,li,blockquote{
                  -webkit-text-size-adjust:100%;
                  -ms-text-size-adjust:100%;
              }
              table,td{
                  mso-table-lspace:0pt;
                  mso-table-rspace:0pt;
              }
              img{
                  -ms-interpolation-mode:bicubic;
              }
              body{
                  margin:0;
                  padding:0;
              }
              img{
                  border:0;
                  height:auto;
                  line-height:100%;
                  outline:none;
                  text-decoration:none;
              }
              table{
                  border-collapse:collapse !important;
              }
              body,#bodyTable,#bodyCell{
                  height:100% !important;
                  margin:0;
                  padding:0;
                  width:100% !important;
              }
              #bodyCell{
                  padding:0;
              }
              #templateContainer{
                  width:100%;
              }

              body,#bodyTable{
                  background-color:#F2F2F2;
                  font-family:'Open Sans', 'Roboto', 'Helvetica Neue', Helvetica, sans-serif;
              }
              h1{
                  color:#202020 !important;
                  display:block;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:26px;
                  font-style:normal;
                  font-weight:bold;
                  line-height:100%;
                  letter-spacing:normal;
                  margin-top:0;
                  margin-right:0;
                  margin-bottom:10px;
                  margin-left:0;
                  text-align:left;
              }
              h2{
                  color:#404040 !important;
                  display:block;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:20px;
                  font-style:normal;
                  font-weight:bold;
                  line-height:100%;
                  letter-spacing:normal;
                  margin-top:20px;
                  margin-right:0;
                  margin-bottom:10px;
                  margin-left:0;
                  text-align:left;
              }

              h2 a {
                color:#404040 !important;
              }

              h3{
                  color:#606060 !important;
                  display:block;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:16px;
                  font-style:italic;
                  font-weight:normal;
                  line-height:100%;
                  letter-spacing:normal;
                  margin-top:0;
                  margin-right:0;
                  margin-bottom:10px;
                  margin-left:0;
                  text-align:left;
              }
              h4{
                  color:#4A4A4A !important;
                  display:block;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:16px;
                  font-style:normal;
                  font-weight:bold;
                  line-height:100%;
                  letter-spacing:normal;
                  margin-top:0;
                  margin-right:0;
                  margin-bottom:0;
                  margin-left:0;
                  text-align:left;
              }
              .headerLogo{
                  margin-bottom:6px;
              }
              .linkTitle{
                  color:#0099ED !important;
              }
              p{
                  padding-top:10px;
                  padding-bottom:10px;
                  margin-top:0;
                  margin-bottom:0;
              }
              ul{
                  margin:0;
                  padding-top:10px;
                  padding-bottom:10px;
                  padding-left:0;
                  padding-right:0;
                  list-style-position:inside;
              }
              .preheaderContent{
                  color:#bfbfbf;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:10px;
                  line-height:40px;
                  text-align:center;
              }
              .preheaderContent a:link,.preheaderContent a:visited,.preheaderContent a .yshortcuts {
                  color:#bfbfbf;
                  font-weight:normal;
                  text-decoration:underline;
              }

              #templateHeader{
                  background-color:#0099ED;
              }
              .headerContent{
                  color:#FFFFFF;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:20px;
                  font-weight:bold;
                  line-height:100%;
                  height:120px;
                  padding-top:24px;
                  padding-right:40px;
                  padding-bottom:0;
                  padding-left:40px;
                  text-align:center;
                  vertical-align:middle;
              }
              .headerContent img {
                width:164px !important;
                height:22px !important;
              }
              .headerContent h1{
                  color:#FFFFFF !important;
                  text-align:center;
                  font-size:22px;
              }
              .headerContent h2{
                  color:#CCEBFB !important;
                  text-align:center;
                  font-weight:200;
                  font-size:16px;
                  margin-top:0;
              }
              .headerContent a:link,.headerContent a:visited,.headerContent a .yshortcuts {
                  color:#EB4102;
                  font-weight:normal;
                  text-decoration:underline;
              }
              #templateBody{
                  background-color:#FFFFFF;
              }

              .bodyContent{
                  color:#505050;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:14px;
                  line-height:22px;
                  padding:0;
                  text-align:left;
              }
              .contentRow{
                  padding-top:20px;
                  padding-left:40px;
                  padding-right:40px;
                  padding-bottom:0;
              }
              .contentRowNoPadding{
                  padding-top:14px;
                  padding-left:0;
                  padding-right:0;
                  padding-bottom:14px;
              }
              .contentCentered{
                  padding-left:20%;
                  padding-right:20%;
                  padding-top:50px;
                  padding-bottom:14px;
                  text-align:center !important;
                  border-top:1px solid #F2F2F2;
                  border-bottom:1px solid #F2F2F2;
                  background:#FAFAFA;
              }
              .blueButton{
                  color:#FFF !important;
                  font-weight:bold;
                  font-size:16px;
                  background:#0099ED;
                  padding-top:12px;
                  padding-bottom:12px;
                  padding-left:16px;
                  padding-right:16px;
                  border-radius:4px;
                  display:inline;
              }
              .label{
                  margin-top:10px;
                  margin-bottom:10px;
                  font-size:13px;
                  line-height:16px;
              }
              .emailImage{
                  height:auto !important;
                  width:100% !important;
                  margin-bottom:10px !important;
              }
              .lastRow{
                  padding-bottom:20px;
              }
              .bodyContent a:link,.bodyContent a:visited,.bodyContent a .yshortcuts {
                  color:#0099ED;
                  font-weight:bold;
                  text-decoration:none;
              }
              .bodyContent img{
                  display:inline;
                  height:auto;
              }

              #templateFooter{
                background-color:#FFFFFF;
              }
              .footerContent{
                  color:#808080;
                  font-family:'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;
                  font-size:10px;
                  line-height:150%;
                  padding-top:60px;
                  padding-right:20px;
                  padding-bottom:20px;
                  padding-left:20px;
                  text-align:center;
              }
              .nitrousLogo{
                  margin-top:20px !important;
                  display:block !important;
              }
              .footerContent a:link,.footerContent a:visited,.footerContent a .yshortcuts,.footerContent a span {
                  color:#606060;
                  font-weight:normal;
                  text-decoration:underline;
              }


          @media only screen and (min-width: 800px){
            #bodyCell{
                padding:20px !important;
            }

            #templateContainer{
                width:600px !important;
            }

            #templateHeader{
                border-radius:4px 4px 0 0 !important;
            }

            .contentRow{
                padding-top:20px !important;
                padding-right:40px !important;
                padding-left:40px !important;
                padding-bottom:6px !important;
            }

            .lastRow{
                padding-bottom:30px !important;
            }
          }

        @media only screen and (max-width: 480px){
              body,table,td,p,a,li,blockquote{
                  -webkit-text-size-adjust:none !important;
              }
              body{
                  width:100% !important;
                  min-width:100% !important;
              }
              #bodyCell{
                  padding:0 !important;
              }
              #templateHeader{
                  border-radius:0 0 0 0 !important;
              }
              .contentRow{
                  padding-left:20px !important;
                  padding-right:20px !important;
              }
              .contentCentered{
                  padding-left:20px !important;
                  padding-right:20px !important;
              }
              #templateContainer{
                  max-width:600px !important;
                  width:100% !important;
              }
              h1{
                  font-size:20px !important;
                  line-height:110% !important;
              }
              h2{
                  font-size:16px !important;
                  line-height:110% !important;
              }
              h3{
                  font-size:18px !important;
                  line-height:100% !important;
              }
              h4{
                  font-size:16px !important;
                  line-height:100% !important;
              }
              #templatePreheader{
                  display:none !important;
              }
              .headerContent{
                  height:120px !important;
                  padding-top:20px !important;
              }
              #headerImage{
                  height:auto !important;
                  max-width:600px !important;
                  width:100% !important;
              }
              .headerContent{
                  font-size:20px !important;
                  line-height:125% !important;
              }
              .bodyContent{
                  font-size:15px !important;
                  line-height:150% !important;
              }

              h4{
                  font-size:15px !important;
                  text-align:left !important;
              }

              .innerContent .bodyContent{
                  text-align:left !important;
                  padding-left:0 !important;
                  padding-right:0 !important;
              }
              .leftImage{
                  display:none !important;
              }
              .rightText{
                  text-align:center !important;
              }
              .footerContent{
                  font-size:14px !important;
                  line-height:115% !important;
              }
              .footerContent a{
                  display:block !important;
              }

          }
        </style>
      </head>

      <body style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;margin: 0;padding: 0;background-color: #F2F2F2;font-family: 'Open Sans', 'Roboto', 'Helvetica Neue', Helvetica, sans-serif;height: 100% !important;width: 100% !important;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" id="bodyTable" width="100%" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;margin: 0;padding: 0;background-color: #FFFFFF;font-family: 'Open Sans', 'Roboto', 'Helvetica Neue', Helvetica, sans-serif;border-collapse: collapse !important;height: 100% !important;width: 100% !important;">
          <tr>
            <td align="center" id="bodyCell" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;margin: 0;padding: 0;height: 100% !important;width: 100% !important;">

              <table border="0" cellpadding="0" cellspacing="0" id="templateContainer" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;width: 100%;border-collapse: collapse !important;">
                <tr>
                  <td align="center" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;">

                    <table border="0" cellpadding="0" cellspacing="0" id="templateHeader" width="100%" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;background-color: #0099ED;border-collapse: collapse !important;">
                      <tr>
                        <td class="headerContent" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;color: #FFFFFF;font-family: 'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;font-size: 20px;font-weight: bold;line-height: 100%;height: 120px;padding-top: 24px;padding-right: 40px;padding-bottom: 0;padding-left: 40px;text-align: center;vertical-align: middle;">
                          <h1>'''+self.email_title+'''</h1>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>

                <tr>
                  <td align="center" class="bodyContent" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;color: #505050;font-family: 'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;font-size: 14px;line-height: 22px;padding: 20px;text-align: left;">

      <br>

      '''\
    +self.generate_header()\
    +self.generate_summary()\
    +self.generate_table()\
    +'''

      </td>
                      </tr>

                    </table>
                  </td>
                </tr>

                <tr>
                  <td align="center" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;">

                    <table border="0" cellpadding="0" cellspacing="0" id="templateFooter" width="100%" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;background-color: #FFFFFF;border-collapse: collapse !important;">
                      <tr>
                        <td class="footerContent" valign="top" style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;color: #808080;font-family: 'Open Sans', 'Helvetica Neue', Helvetica, sans-serif;font-size: 10px;line-height: 150%;padding-top: 60px;padding-right: 20px;padding-bottom: 20px;padding-left: 20px;text-align: center;">
                          <a href="mailto:channeng@hotmail.com?Subject=Unsubscribe%20from%20Events%20Notification" target="_blank" style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; color: #606060; font-weight: normal; text-decoration: underline;">Unsubscribe</a>
                          <p style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;padding-top: 10px;padding-bottom: 10px;margin-top: 0;margin-bottom: 0;">Copyright &copy; 2015, All rights reserved.</p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </body>
      </html>'''
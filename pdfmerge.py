# Python Source Code
        ######## Section A #########
        # specify App SID
AsposeApp.app_sid = '5a******-***-***-8a***'
        # Specify App Key
AsposeApp.app_key = '***********3g'
        # build URI  to merge PDFs
str_uri = 'http://api.aspose.com/v1.1/words/MainDocument.docx/appendDocument'
        # sign URI
signed_uri = Utils.sign(Utils(), str_uri)

        ######## End Section A #########


        ######## Section B ##########
        #Build JSON to post
        json_document1 = json.dumps({'Href' : 'AppendDocument1.docx',
'ImportFormatMode' : 'KeepSourceFormatting'})
        json_document2 = json.dumps({'Href' : 'AppendDocument2.docx',
'ImportFormatMode' : 'UseDestinationStyles'})
json_arr = '{\'DocumentEntries\':[' + json_document1 + ',' + json_document2 +
']}'

        ######### End Section B ########

            ##### Section C ######
Utils.process_command(Utils(), signed_uri, 'POST', 'JSON', json_arr)
            ##### End Section C ######                
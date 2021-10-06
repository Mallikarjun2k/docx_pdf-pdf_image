import os
import win32com.client

wdFormatPDF = 17

for root, dirs, files in os.walk(r'C:\Users\Admin\OneDrive\Desktop\VS Projects\CV\New folder'):
    for f in files:

        if  f.endswith(".doc"):
            try:
                print(f)
                in_file=os.path.join(root,f)
                word = win32com.client.Dispatch('Word.Application')
                word.Visible = False
                doc = word.Documents.Open(in_file)
                doc.SaveAs(os.path.join(root,f[:-4]), FileFormat=wdFormatPDF)
                doc.Close()
                word.Quit()
                word.Visible = True
                print ('done')
                os.remove(os.path.join(root,f))
                pass
            except:
                print('could not open')
                # os.remove(os.path.join(root,f))
        elif f.endswith(".docx"):
            try:
                print(f)
                in_file=os.path.join(root,f)
                word = win32com.client.Dispatch('Word.Application')
                word.Visible = False
                doc = word.Documents.Open(in_file)
                doc.SaveAs(os.path.join(root,f[:-5]), FileFormat=wdFormatPDF)
                doc.Close()
                word.Quit()
                word.Visible = True
                print ('done')
                os.remove(os.path.join(root,f))
                pass
            except:
                print('could not open')
                # os.remove(os.path.join(root,f))
        else:
            pass
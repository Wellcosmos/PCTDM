def clear_badchart(source_dir,desc_dir): #将xml中的非法字符清除
    print (time.strftime('%Y-%m-%d %H:%M:%S'))
    n=1
    for filename in os.listdir(source_dir):
        if filename.find('.xml') == -1:
            continue
        print(filename)
        w_file=codecs.open(desc_dir+'//'+filename, 'w', encoding='utf-8')
        r_file=codecs.open(os.path.join(source_dir,filename), 'rb', encoding='utf-8')
        for text in r_file :
            text=re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+","VVVV",text)
            #text=re.sub("[^\u0020-\u9FA5]", "OOOO",text)
            text=re.sub("<br/>","",text)
            w_file.writelines(text)

        n+=1
        #w_file.close()
    print(n,' files cleared.')
    print (time.strftime('%Y-%m-%d %H:%M:%S'))

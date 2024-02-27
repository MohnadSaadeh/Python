def varargs(arg1 ,*args):
    print("Got", arg1 , " and " ,args)
    for x in args:
        print(x)



varargs("one")
varargs("one","two")
varargs("one","two","three")
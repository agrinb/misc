def echo(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            try:
                value = (yield value)
                print(value)
            except Exception, e:
                value = e
    finally:
        print "Don't forget to clean up when 'close()' is called."

generator = echo(1)
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.send(2)
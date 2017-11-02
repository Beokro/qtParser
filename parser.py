import sys
import operator

def getTimeDiff( start, end ):
    startList = start.split( ':' )
    endList = end.split( ':' )
    if len( startList ) != 3 or len( endList ) != 3:
        print start + " . " + end
        assert( 0 )
    startSec = float( startList[ 2 ] )
    endSec = float( endList[ 2 ] )
    if startList[ 1 ] != endList[ 1 ]:
        endSec += 60
    return endSec - startSec

def getFunctionName( msg ):
    list = msg.split( ' ' )
    type = list[ 0 ]
    name = ''
    if type == 'void':
        name = type + ' ' + list[ 1 ]
    elif type == 'virtual':
        name = type + ' ' + list[ 1 ] + ' ' + list[ 2 ]
    return name

def main():
    if len( sys.argv ) < 2:
        print 'Log file name is needed'
        exit()

    fileName = sys.argv[ 1 ]

    freq = {}
    timeTaken = {}
    lastTime = '15:41:41.891882'
    currentTime = ''
    timeDiff = 0
    message = ''
    funName = ''


    with open( fileName ) as fp:
        for line in fp:
            list = line.split( ' ' )
            currentTime = list[ 1 ]
            message = line.split( '\"' )[ 1 ]
            funName = getFunctionName( message )
            timeDiff = getTimeDiff( lastTime, currentTime )
            lastTime = currentTime

            if funName == '':
                continue

            if funName not in freq:
                freq[ funName ] = 0
            freq[ funName ] += 1

            if funName not in timeTaken:
                timeTaken[ funName ] = 0.0
            timeTaken[ funName ] += timeDiff

            '''
            print line
            print timeDiff
            print list
            print currentTime
            print message
            print funName
            '''

    sorted_freq = sorted( freq.items(), key=operator.itemgetter(1) )
    for ( name, frequencies ) in sorted_freq:
        print name + '  ' + str( frequencies )


    sorted_timeTaken = sorted( timeTaken.items(), key=operator.itemgetter(1) )
    for ( name, timeTakenuens ) in sorted_timeTaken:
        print name + '  ' + str( timeTakenuens )

main()

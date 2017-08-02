from mrjob.job import MRJob
import track

class SuggestUltimate(MRJob):
    
    print "This is mortify"

    print "What tempo do you like\n\t 1 : High\n\t 2 : Mid\n\t 3 : Low"
    tempo=input()

    print "\nWhat about loudness\n\t 1 : High\n\t 2 : Mid\n\t 3 : Low"
    loudness=input()

    print "\nAnd what about danceability\n\t 1 : I dance\n\t 2 : I dont\n\t 3 : whatever"
    danceability=input()

    if(tempo==1):
        global thigh
        thigh=90
        global tlow
        tlow=60
    elif(tempo==2):
        global thigh
        thigh=30
        global tlow
        tlow=59
    else:
        global thigh
        thigh=29
        global tlow
        tlow=0

    if(loudness==1):
        global lhigh
        lhigh=0
        global llow
        llow=-4
    elif(loudness==2):
        global lhigh
        lhigh=-4
        global llow
        llow=-9
    else:
        global lhigh
        lhigh=-9
        global llow
        llow=-100

    if(danceability==1):
        global dance
        dance=1
    else:
        global dance
        dance=0

    def mapper(self, _, line):

            """ The mapper loads a track and yields similar songs """
            t = track.load_track(line)
            i=1
            if t:
                if (t['tempo'] > tlow and t['tempo'] < thigh) or (t['loudness'] > llow and t['loudness'] < lhigh):
                    yield i, (t['artist_name'], t['title'], t['tempo'], t['loudness'], t['danceability'])
                    i+=1

                    

if __name__ == '__main__':
    SuggestUltimate.run()
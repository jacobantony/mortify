Mortify
===========


These examples depend on mrjob, a python library for running MapReduce jobs on Hadoop or Amazon web services.  See
https://github.com/Yelp/mrjob and http://packages.python.org/mrjob/.


MSD Data on S3
==============
These examples use MSD data that has been loaded on to S3 at s3://tbmmsd.  There are around 330 files each with about 3000
sets track data each (one set per line) where each line is represented by 54 fields as described here:  
    
 http://labrosa.ee.columbia.edu/millionsong/pages/field-list

except that in the flat file format, the 'track id' field has been moved from field 52 to the first field.

In the repository you will find tiny.dat which contains data for 20 tracks.




Map-reduce jobs
===============

Density
------
Finds the most dense and the least dense songs

density.py


### Local Usage:

    python density.py tiny.dat


### EC2 Usage
This will run the job on EC2 Map reduce on 100 small instances. Note that you have to 
add the track.py code to t.tar.gz with:

    % tar cvfz t.tar.gz track.py

To run the job on 100 CPUs on all of the MSD use:     

    %  python density.py --num-ec2-instances 100 --python-archive t.tar.gz -r emr 's3://tbmmsd/*.tsv.*' > output.dat


(Of course you will need to setup your Amazon credentials. See http://packages.python.org/mrjob/writing-and-running.html#running-on-emr )



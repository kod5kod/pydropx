
# -*- coding: utf-8 -*-
"""
#### pydropx v0.01 Beta #####
Created on Thursday, January  21  10:02:04 2016
@author: Datuman a.k.a. kod5kod
https://github.com/kod5kod

The "pydropx" module is a  simple dropbox wrapper for uploading files and folders.

Required config dictionary

"""

import dropbox
import os



def dropbox_api(conf):
        '''Returns connection to dropbox api'''
        return dropbox.client.DropboxClient(conf['dropbox_access_token'])


def upload_file(source, dest, client=dropbox_api(conf)):

        """uploads a file to a specific destination on dropbox

        @param str, path to file locally
        @param str, path to destination on dropbox
        @param dropbox_conn, connection to dropbox api
        """

        f = open(source, 'rb')
        client.put_file(dest, f)

def upload_directory(source, dest, client=dropbox_api(conf)):
        '''Uploads all files in a directory to a given directory on dropbox.
        This retains the same file structure present locally under the new destination folder/.
        Eg. source/dir/file.txt would get sent to dest/dir/file.txt

        @param str, path to local dest
        @param str, path to destination on dropbox
        @param dropbox_conn, connection to dropbox api
        '''

        for f in os.walk(source):
                for i in f[2]:
                        source_file = os.path.join(f[0], i)
                        print dest+'/'+source_file[len(source):]
                        upload_file(source_file,dest+'/'+source_file[len(source):],client=client)

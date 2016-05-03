# nom-noms

# Initial setup (for posterity):
create app in github
create app in c9 from github link
create app.yaml
https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
cd ~
wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.35.zip
unzip google_appengine_1.9.35.zip
rm google_appengine_1.9.35.zip
export PATH=$PATH:/home/ubuntu/google_appengine/
and add above .bashrc
/usr/bin/env python -V
create google cloud project
https://cloud.google.com/appengine/docs/python/tools/uploadinganapp
appcfg.py update --noauth_local_webserver workspace

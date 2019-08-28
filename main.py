import flask
from flask import make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/', methods=['GET'])
def home():
    caps_template = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <caps>
     <server appversion="0.8.4.0" version="0.1" title="NZB Finder" strapline="Fast, Easy, Reliable" email="hello@nzbfinder.ws" meta="usenet,nzbs,newznab,indexer,indexing,index,couchpotato,sickbeard,alt.binaries,alt.binaries.hdtv,bluray,blu-ray" url="https://nzbfinder.ws/" image="https://nzbfinder.ws/themes/shared/images/logo.png"/>
     <limits max="100" default="100"/>
     <registration available="yes" open="yes"/>
     <searching>
      <search available="yes" supportedParams="q"/>
      <tv-search available="yes" supportedParams="q,vid,tvdbid,traktid,rid,tvmazeid,imdbid,tmdbid,season,ep"/>
      <movie-search available="yes" supportedParams="q,imdbid"/>
      <audio-search available="no" supportedParams=""/>
     </searching>
     <categories>
      <category id="2000" name="Movies">
       <subcat id="2050" name="3D"/>
       <subcat id="2060" name="BluRay"/>
       <subcat id="2070" name="DVD"/>
       <subcat id="2010" name="Foreign"/>
       <subcat id="2040" name="HD"/>
       <subcat id="2999" name="Other"/>
       <subcat id="2030" name="SD"/>
       <subcat id="2045" name="UHD"/>
      </category>
      <category id="3000" name="Audio">
       <subcat id="3030" name="Audiobook"/>
       <subcat id="3060" name="Foreign"/>
       <subcat id="3040" name="Lossless"/>
       <subcat id="3010" name="MP3"/>
       <subcat id="3999" name="Other"/>
       <subcat id="3020" name="Video"/>
      </category>
      <category id="5000" name="TV">
       <subcat id="5070" name="Anime"/>
       <subcat id="5080" name="Documentary"/>
       <subcat id="5020" name="Foreign"/>
       <subcat id="5040" name="HD"/>
       <subcat id="5999" name="Other"/>
       <subcat id="5030" name="SD"/>
       <subcat id="5060" name="Sport"/>
       <subcat id="5045" name="UHD"/>
      </category>
      <category id="6000" name="XXX">
       <subcat id="6010" name="DVD"/>
       <subcat id="6060" name="Imageset"/>
       <subcat id="6999" name="Other"/>
       <subcat id="6070" name="Packs"/>
       <subcat id="6080" name="SD"/>
       <subcat id="6045" name="UHD"/>
       <subcat id="6020" name="WMV"/>
       <subcat id="6030" name="XviD"/>
       <subcat id="6040" name="x264"/>
      </category>
      <category id="7000" name="Books">
       <subcat id="7030" name="Comics"/>
       <subcat id="7020" name="Ebook"/>
       <subcat id="7060" name="Foreign"/>
       <subcat id="7010" name="Magazines"/>
       <subcat id="7999" name="Other"/>
       <subcat id="7040" name="Technical"/>
      </category>
      <category id="0" name="Other">
       <subcat id="20" name="Hashed"/>
       <subcat id="10" name="Misc"/>
      </category>
     </categories>
    </caps>
    """
    response = make_response(caps_template)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/', methods=['GET'])
def home():
    title = "Es war einmal ein Deadpool 2018 German DL AC3 Dubbed 1080p BluRay x264-PsO"
    xmlTemplate = f"""<?xml version="1.0" encoding="utf-8" ?>
    <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:newznab="http://www.newznab.com/DTD/2010/feeds/attributes/">
      <channel>
        <atom:link href="http://nzb.su/api?t=tvsearch&amp;cat=5030,5040&amp;apikey=xxx" rel="self" type="application/rss+xml" />
        <title>Nzb.su</title>
        <description>Nzb.su Feed</description>
        <link>http://nzb.su/</link>
        <language>en-gb</language>
        <webMaster>root@nzb.su (Nzb.su)</webMaster>
        <category></category>
        <image>
          <url>http://nzb.su/views/images/banner.jpg</url>
    
          <title>Nzb.su</title>
          <link>http://nzb.su/</link>
          <description>Visit Nzb.su - indexing usenet one part at a time</description>
        </image>
    
        <newznab:response offset="0" total="10000" />
        <item>
          <title>{title}</title>
    
          <guid isPermaLink="true">http://nzb.su/details/66c5ikv9aKRydXY0bY77</guid>
          <link>http://nzb.su/getnzb/24967ef4c2e26296c65d3bbfa97aa8fe.nzb&amp;i=37292&amp;r=xxx</link>
          <pubDate>Mon, 16 Jan 2019 10:45:00 -0500</pubDate>
          <category>Movie &gt; HD</category>
          <description>{title}</description>
          <enclosure url="http://nzb.su/getnzb/24967ef4c2e26296c65d3bbfa97aa8fe.nzb&amp;i=37292&amp;r=xxx" length="1183105773" type="application/x-nzb" />
          
          <newznab:attr name="category" value="2040" />
          <newznab:attr name="category" value="2010" />
          <newznab:attr name="size" value="8235599790" />
          <newznab:attr name="guid" value="66c5ikv9aKRydXY0bY77" />
        </item>
      </channel>
    </rss>
        """
    response = make_response(xmlTemplate)
    response.headers["Content-Type"] = "application/xml"
    return response


app.run()

import urllib, urllib2, json, time
from Bio import SeqIO
from sys import argv

# install a custom handler to prevent following of redirects automatically.
class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return headers
opener = urllib2.build_opener(SmartRedirectHandler())
urllib2.install_opener(opener)

out_file = open("phmmer_description.tab", 'wa')

for sequence in SeqIO.parse(open(argv[1], 'r'), 'fasta'):
    parameters = {
                  'seqdb':'uniprotkb',
                  'seq':'>{0}\n{1}'.format(sequence.id, str(sequence.seq))
                 }
    enc_params = urllib.urlencode(parameters)

    #post the seqrch request to the server
    request = urllib2.Request('http://hmmer.janelia.org/search/phmmer',enc_params)

    #get the url where the results can be fetched from
    results_url = urllib2.urlopen(request).getheader('location')

    # modify the range, format and presence of alignments in your results here
    res_params = {
                  'output':'json',
                  'range':'1,10'
                 }

    # add the parameters to your request for the results
    enc_res_params = urllib.urlencode(res_params)
    modified_res_url = results_url + '?' + enc_res_params

    # send a GET request to the server
    results_request = urllib2.Request(modified_res_url)
    data = urllib2.urlopen(results_request)

    # print out the results
    parsed_data =  json.loads(data.read())

    descriptions = []
    for hit in parsed_data['results']['hits']:
        descriptions.append(hit['desc'])

    output =  "{0}\t{1}\n".format(sequence.id, '\t'.join(descriptions))
    out_file.write(output)
    time.sleep(10)


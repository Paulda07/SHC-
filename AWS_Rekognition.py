import boto3

if __name__ == "__main__":

    bucket='bucketdetectcards'
    photo='zeamed_card.png'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            if len(text['DetectedText'])== 20 and text['DetectedText'][0:3] == 'ZEA':
                print ('Detected text:' + text['DetectedText'])
                print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                print ('Id: {}'.format(text['Id']))
                if 'ParentId' in text:
                    print ('Parent Id: {}'.format(text['ParentId']))
                print ('Type:' + text['Type'])



                
    
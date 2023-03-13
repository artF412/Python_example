import os

def resolvePath (filesExtension,purpose,version):
    # get environment variables
    envS = os.getenv('show')
    envA = os.getenv('asset')
    
    # print path
    print('/mnt/nfs/projects/'+envS+'/'+envA+'/'+filesExtension+'/'+purpose+'/'+version)

resolvePath('filesExtension','purpose','version')
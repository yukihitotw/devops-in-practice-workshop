#!/usr/bin/env python
from gomatic import *
import os, re

go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
pipeline = configurator\
        .ensure_pipeline_group("sample")\
        .ensure_replacement_of_pipeline("PetClinic")\
        .set_git_material(GitMaterial("https://github.com/yukihitotw/devops-in-practice-workshop.git", ignore_patterns=set(['pipelines/*']))).ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-123-227513'}).ensure_encrypted_environment_variables({'GCLOUD_SERVICE_KEY': 'AES:2j9nrBio/CWRCc3rEaQ/GQ==:vu5SMwU8TsRk+xkMBDMVT5IQ1UuG1MZG8OZETensKNqn5WY85AMQhM2PVlItVeoOCM3kI5Wd+a0kltKCs9FNrLuDk+huqPgoQ6yV9WAjDUGXPhVWj933GXmBSnAxDjgWoijJuHZGlE1L7wIc3vhaP7r/PR5GjrP4skCg4AuSi0DJqVsi4mYbn1zNt+oOkstrGy0miACang0BJGZKnvlUsga6r1LVBqrnX0aisCAuPv2uFrGsXQdDx+SAmFAiNFhkCUHh7cR76MeBs//SpC32wHhw8CFVz65ksiSpIqbmE8edSE72nNMwQyuJqh4oQ94/sdgx39oF0a1lDZmHs2DcDpQVWywKx/H1RS5oysR+7Sx7324JUPYz7QOZCm4sqAbvUnH9J1hpymqt0P8IJt1Gv8Ioy7a6qwUZHsx9+El/oM+065BFEwxfMPiZsyJNsGMNBDiJ2RrghGgCmOZqJqW8uUofTNuqkW+qAK7CzurZEkbxqucUXG2wiFhyzxaAInWNuhlWzpfQLnDIBNe0Q9JZL0uIKJyHeWLtP62UYSDNwRSSwtxAev7bO7/w46IOfbqQB2oWZWghKV8bgumGZSzM4Huc9O+gDTYb30ImhsvFRnP4eGA73uhnQtx1QTVfLB5HOMWEy8CwpyhJ/Hn+mjgnBeOAvCGCp+uwWInqd5jZxHz+KpWmwxnkGPGdgmBU+zlUahlgzC9us70Nb+X74Y8Cq8nn+EJVzD1uyVaBKvTFhGU3lKbtwcIcY7y/zfwWUEg+XZ5SxcJBQ3Wi1uCMD2LifYt9VCIzqjR5tq+nRVyBKszU+CUCvjCM4WZ9pFHRIpTCyB80PAv+wpq9Vmsz5H8S/MmpGr7NdxMqjLWlwlMSfMSd5tBezyqI8VMZ3WOokyv9+g7A2Aky9Q8TQu+G4XBPd22ZpecOWmQQotKgFkJ8eBkXAbP81jqy624sE421FvH0Q8fJyHlzqrx6UZvNsuww4ErwGBfr6TWaFXXFHsAWYtgiblkaFSpFBCqhlSTg+xLbLsg3d70MqRM6tarMuF8ISe8kKXzVdu/ifLgHS5vjeR5FA/HHii+F7eMEdUxHGYBjCKN3Dtf1+VxtuX2mnjChdvko/OywI5B+9D1YAbJHdb/3PaFm1QeT8ufazBDwmxuhZJ8Tu8h99/wpdBRrxSVnikzrCGef1EIjZRs5va53EHMpBIX1q3SsTWQ0qRWu58jprDMFuHhVZvWbpPIrMD7qESqCrWk1tk4XyByrRlNYYbZ+m6bUHCHrPCuaS8q4tEE1YWjhHNKHUaGOf0PuFd9irQ2GSSjJPije5FmYk+9+99ss7QQC3ZK8sU3WFonDgw4PHjt1Tlsy/XJvdC5DZPGyRx+lKHGzmboHWbq2DQDfcQ4iB5BaMWlhCdP1go+y7VV3V/z6HVddQdhZPuN0zkR6SLGckeSBLulO7A9vYSUDXg/w/Nyn7F/WMb7eibpuvvudMvUfVP9Zr3iBY049ipzeI0BvKK6oLundWDPk+LtkUwfdcg2pvePL63jh8/9wvfeBewtVzGcp8K1L/3W9yu96y12Jxf0ii3AInkkjYZpUiUiHSoMrhZ8kXmKSz781bQBAsbW/CPBy9333i4pfSFKF81Q+BMDNe0XumPpIHlFwax62PXw0DE42AN2uPyM7uhknLksRCYDeylRqKV5eyavfAku9dNipAjHDcGz7hZSOCJd1U1Hp46KFAJ732SPSrIvgazpZhg7LebaYehAGQ2xOqqzH91LBb8ylAW4M2jlS8GpJAjqyGliERsAU0wzYs+dits2S+wpaddYweRYAIMqs99d+CgABHqeSXeejTNa8eVf055DjonINmKAUIJBszwJWNAICqdyVrUFDfpnTxPSJWYq6pyiB0JidblqpPwV/nnCZyUFaf9tLDOPThBxLSHwOz4+IRId40MrBNXI5AhWVznjmJWFuvGsduk4m/HuFN1IzCgNC/YNYN6MF4/eE3oiHa8lp5kvdvGtbSt4P0HZEv72v04tlb6Lk5czVkAPCQMlt9+6Pk0aZP9xMIFaOUTCIAyhT4urPVoZ9fQLSBkwvjqlUiXLAx1WA5/F5sEcHIvlNeq+hQUiVlh4AJpULeDz+v66sUNx/2Nm3WY0apVbeJzBZikDKIwqgenqomHDTQ8Cf6WK4y7kn8zWXhSYza2y+C5nhrdw71VEXyM4SqM7Ldg6VqQwZWvlxmypZ2TAcIRvVvk6eyRVmh9WCBytJQuwo0w7P5vPsA2JM2cEy1hPokRtYEPs11qlZwj+IIYdvAhHC3Ad8Uw5VBln5SvnmF1I2h48A9wDEjD4fkIhfcDTfK08RsDcRqBjioEshfDUSxI7SFPZV20NuYPOtBqASwCZytZcsS7zkyoH9heCLhoQUAZ0EkFWd+s/eiWUVc+TgALticnKDOOisAAhdExVTR8DdQRB1SG4MkVC2IDQCqzUhP/MVyAbugdQxSiSZDc2GpWVMcn+jKHujfBYsxxsdn736+NWe2G52T7NHa7ud+cJ2mYH7nWk4oKxH53/pwdP16/wdoBRGS5ueadeKJpQTmxNe2JZ5mqAr5lClerK/cnUzwLcXiveyZVX4xtcxrqH5Q5EeTKB2QzuEF3IbRU7yoHMt9FYNsLhPidnwd1B3z8CFTKQIYmjiS4qSolCaOVjx4dMRhQE89m+xVqWzaxiFNoI0fqB9/BxUzr6PzwoAPbqALP9RK1SiaygTTbDXRSjX9Wz7IZvjjzQg5LRpdxmxPAbFizFYZOJQke4cMVUAVna8DvUuZLPFyX6IPgw0c91W7oaNsWhNpgPWZVMr6WdIxw5HbUmhfZAWRCXrJMP8R+oq8HirmaLsin0cxLtDeGaIpsJZPe7/W2kZTyAyBvG2h5SZib/7sp10JTSee8k/TbaeoeXRRXizHTpy1d8Kh9qnjHba/Lz8YEIAX7xy3wBk4PKLY2yktus8rLjs45wWcX2D4YzWgKL6hGhMbPIH2LrLQ1q5gkPQAr3zgBbszGKZQuP6H0Ns7gYEPM9yf1dp0oCkAus2RPEMfsL37jaiswLDyD70yTb/wUngz7WAqz8saVTFVe0luSc7LzGuRPdSri6y71XVxAt9hheO2fasLmm+86PBVnNxd5DaIKDqtlPWncxwVNfnxL3VlHeQdvTKRkVTlwrklFPL37iLzC+U71yac+57cM6LsdalY9qYgtU38SzJWMzhvRJNCpgsuNobQ6qob3h8RrESpFdQQ48at+ybGasSPhDAglsz+CkGko4jJFnS2cODqQIuM6jrLxTHUAUuGJ4yXgMwh6/v/J2astG7KVkcQoWQzWpK7yEb+jE9YFPDFYZPsKGEKNyetDKAiTtMcjpE9sDYgOj0fDFVqq+j60/iFgErwu+AyrVZgDYQZKtdyB57DkiTWXY99e2Pf4c5oiwlTSWLHIag+Vt4WSCin08R/aaEluu/9x9AlGZ7mPNhJ89JCMwx7nfgsIYTobeYqFsoLn0juccSfITq9v0jToQjo52cVazf2dRU0eHsijqPsIKu/TRc7RpH5mmgEPmZE4KnWJDFDqrsRGoQTGY0L82P6S/dfib7mhNDewKqC8lSwhgP4l/ZsNzMrvtnBSvO/1gQJm/dtPhnnOtk1YSegvStCaGwmpp2x5X2I1MLs20Q0Zw0CeKdlW35T50pEQu2A6PqbxRrBHBf4a1uIpJ4pILu1uBItpUUnk6NNtgCawiAI0D8MLR8evk1uX/2TuWGS1BKY+T+btclHAjINP5TD7Nt7Q59zvophA2Djh4IX1WVVsQBPA71vjg6RyMm8XGl69N/Q3aDirjSsHMCNTahQi0tQSb4iSOsYjlxlOp1haN7tpt9qMdvm8lbus10dr39UDavOr0p2ObO+lgQeQKQd4A+drfVO/RYJafNkoRRNw6Yw2yOw60YgnMBYCu/5N4FQuPmJX0SHnZK7ox36bQhNGhc47ZbTFaWWaUa1OXhL9Ee8aDEZJ7734AaCILE6rLHKvAUFMIRCTHMmL1YIAAmRIWTaZG7TCJhrxYFpDExd36j6BOWWw8hQlnUyJpsyJ9j26s6dFIGIKQrAyfT0ZIlN4z58F+fzCMFhqo1iJMGBozOeTqIebKvGtpQXoE3SzreB7JAsk5N2YvBMxcES7pM6lUqfsnA9ak3mA3qPXuKUMqwscoCqkwWA9NSB6G5gxW/3bzOXvx0JWlkilfoNRu3OWI='})
stage = pipeline.ensure_stage("commit")
job = stage.ensure_job("build-and-publish").set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy").ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123-227513', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})
job = stage.ensure_job("deploy").set_elastic_profile_id("kubectl")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage\
	.ensure_job("complete-canary")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-123', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()

configurator.save_updated_config()


print "Updating PetClinic Pipeline..."

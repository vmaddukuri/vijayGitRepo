

void runStages(String tag) {
    
    docker.image(tag).inside("--privileged=true --user root") {
	
		stage('Git Clone') {

			sh 'git config --global http.proxy https://10.131.236.9:3128/'
			
			sh 'rm -fR enterprise-cloud-connector'
			
			withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'CREDENTIALS_ID_GIT',
							  usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
			
				sh '''git clone http://$USERNAME:$PASSWORD@github.com/virtustream/enterprise-cloud-connector.git'''
			
			}

		}
		
		stage('Copy the POM file'){

			sh '''
				dir=$(pwd)
				cp /opt/ecc/enterprise-cloud-connector/virtustream-vro-plugin/pom.xml $dir/enterprise-cloud-connector/virtustream-vro-plugin/pom.xml
			'''						
		}

		stage('Generate Maven Build'){

			sh '''
			dir=$(pwd)
			mvn -f $dir/enterprise-cloud-connector/virtustream-vro-plugin/pom.xml clean install exec:java -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DskipTests=true -Dbuild.number=1
			'''
		}
		
		stage('Generate SonarQube Report'){

			sh '''
			dir=$(pwd)
			mvn -f $dir/enterprise-cloud-connector/virtustream-vro-plugin/pom.xml -e -B sonar:sonar -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DskipTests=true -Dbuild.number=1 -DproxyHost=10.131.236.9 -DproxyPort=3128 -DproxySet=true -Dsonar.analysis.mode=preview -Dsonar.issuesReport.html.enable=true -Dsonar.host.url=http://10.100.26.124:9000/sonar
			'''
		}
		
		stage('Generate Artifactory') {
		
			def taglist = sh script: 'cd enterprise-cloud-connector/virtustream-vro-plugin/ && git tag', returnStdout: true
			def dir = sh script: 'pwd', returnStdout: true
			def ws = dir.trim();
			def lasttag = ""
				
			String[] splitData = taglist.split("\n");
			for (String eachSplit : splitData) {
				if (eachSplit.startsWith("v")) {
					lasttag = eachSplit.substring(1);
					println lasttag
				}
			}

			withCredentials([usernamePassword(credentialsId: 'Artifactory_Local', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {

				def lastbuild = Jenkins.instance.getItemByFullName("${env.JOB_BASE_NAME}").getLastSuccessfulBuild().toString()
				
				def lastbuildnumber = lastbuild.substring(lastbuild.indexOf('#') + 1)
				
				int newbuildnumber = lastbuildnumber.toInteger() + 1

				def ver = lasttag + "-" + newbuildnumber


				
				sh """
				curl -u $USERNAME:$PASSWORD -T '${ws}/enterprise-cloud-connector/virtustream-vro-plugin/virtustream-ecc-installer/virtustream-ecc-installer-core/target/VECC_v1.0.exe' 'http://10.100.26.124:8081/artifactory/vecc_installer/vecc/VECC_v${ver}.exe'
				"""

			}
		}
	}
}
	
node{

	//checkout scm

	String imageTag
	imageTag = "vijaymaddukuri/maven:latest"

	runStages(imageTag)
  
}

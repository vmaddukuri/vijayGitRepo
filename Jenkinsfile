import static *

void runStages(String tag) {
    
    docker.image(tag).inside("--privileged=true --user root") {
	
		
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

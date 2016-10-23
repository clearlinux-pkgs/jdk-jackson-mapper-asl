PKG_NAME := jdk-jackson-mapper-asl
URL := http://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar
ARCHIVES := http://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.pom %{buildroot}

include ../common/Makefile.common

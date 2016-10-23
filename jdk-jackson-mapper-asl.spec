Name     : jdk-jackson-mapper-asl
Version  : 1.9.13
Release  : 1
URL      : http://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar
Source0  : http://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar
Source1  : http://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-jackson-mapper-asl-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jackson-mapper-asl package.
Group: Data

%description data
data components for the jdk-jackson-mapper-asl package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jackson-mapper-asl.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jackson-mapper-asl.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jackson-mapper-asl.xml \
%{buildroot}/usr/share/maven-poms/jackson-mapper-asl.pom \
%{buildroot}/usr/share/java/jackson-mapper-asl.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jackson-mapper-asl.jar
/usr/share/maven-metadata/jackson-mapper-asl.xml
/usr/share/maven-poms/jackson-mapper-asl.pom

%{?scl:%scl_package geronimo-jms}
%{!?scl:%global pkg_name %{name}}

%{?thermostat_find_provides_and_requires}

%global spec_name geronimo-jms_1.1_spec

Name:		%{?scl_prefix}geronimo-jms
Version:	1.1.1
Release:	18.3%{?dist}
Summary:	J2EE JMS v1.1 API

Group:		Development/Libraries
License:	ASL 2.0
URL:		http://geronimo.apache.org/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/%{spec_name}-%{version}/
Source0:	%{spec_name}-%{version}.tar.bz
# Remove unavailable dependencies
Patch0:		geronimo-jms-1.1-api-remove-mockobjects.patch

BuildArch:	noarch

# This pulls in almost all of the required java and maven stuff
BuildRequires:  maven-local
BuildRequires:	geronimo-parent-poms
BuildRequires:	maven-resources-plugin

# Ensure a smooth transition from geronimo-specs
Provides:	%{?scl_prefix}jms = %{version}-%{release}
Obsoletes:	%{?scl_prefix}geronimo-specs <= 1.0-3.3
Obsoletes:	%{?scl_prefix}geronimo-specs-compat <= 1.0-3.3

%description
The Java Message Service (JMS) API is a messaging standard that allows
application components based on the Java 2 Platform, Enterprise Edition
(J2EE) to create, send, receive, and read messages. It enables distributed
communication that is loosely coupled, reliable, and asynchronous.

%package javadoc
Summary:	API documentation for %{name}
Group:		Documentation
Requires:	jpackage-utils >= 0:1.7.5
BuildArch:	noarch

%description javadoc
%{summary}.

%prep
%{?scl:scl enable %{scl} - << "EOF"}
%setup -q -n %{spec_name}-%{version}
%patch0 -p1
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_file  : %{pkg_name} %{spec_name} jms
%mvn_alias : javax.jms:jms
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 21 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.1-18.3
- Rebuild to fix requires/provides

* Mon Nov 18 2013 Michal Srb <msrb@redhat.com> - 1.1.1-18.2
- Enable SCL for each spec section

* Mon Nov 18 2013 Michal Srb <msrb@redhat.com> - 1.1.1-18.1
- Enable SCL for thermostat
- Remove BuildRoot

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-18
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-17
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-15
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.1.1-14
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-13
- Install LICENSE and NOTICE with javadoc package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.1-10
- Fix forgotten pre scriptlet for javadoc symlink removal

* Thu Nov 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.1-9
- Use maven 3 to build
- Update according to latest guidelines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Alexander Kurtakov <akurtako@redhat.com> 1.1.1-7
- Add javax.jms:jms depmap.

* Fri Apr  2 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-6
- Add the *correct* version to the geronimo-specs Obsoletes line
- Also Obsolete geronimo-specs-compat

* Tue Mar 16 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-5
- Don't require geronimo-parent-poms at runtime

* Wed Feb 10 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-4
- Add a version to the geronimo-specs Obsoletes line

* Wed Feb 10 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-3
- Clean up provides list, and obsolete geronimo-specs
- Change summary and javadoc description

* Wed Feb  3 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-2
- Remove config marker on maven depmap fragment
- Remove gcj
- Move the provides/obsoletes a bit

* Tue Jan 19 2010 Mary Ellen Foster <mefoster at gmail.com> 1.1.1-1
- Initial package

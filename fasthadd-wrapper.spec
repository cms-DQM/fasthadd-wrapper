Name:           fasthadd
Version:        14
Release:        0
License:        GPLv2+
Summary:        A wrapper around fasthadd and hadd utilities
Obsoletes:      fasthadd = 12.0-el7.cern, fasthadd = 11.0-el7.cern, fasthadd = 10.0-el7.cern
%description
A wrapper around hadd utilities (fastHadd is retired). Contains only the files that start the respective program.

%build
%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 /tmp/${USER}/fasthadd/hadd %{buildroot}/usr/bin/hadd

%files
/usr/bin/hadd

%changelog
* Mon Aug 10 2020 Andrius Kirilovas <andrius.kirilovas[at]cern.ch> - 12.0 - Added hadd program to the package.
* Fri Jul 12 2019 Andrius Kirilovas <andrius.kirilovas[at]cern.ch> - 11.0 - An update due to a root version change

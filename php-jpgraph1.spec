Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		jpgraph
Version:	1.12.2
Release:	1
Group:		Libraries
License:	GPL
Source0:	http://jpgraph.techuk.com/jpgraph/downloads/%{name}%{version}.zip
# Source0-md5:	666d934c67fb79f278e7695fd3660f75
Source1:	http://www.aditus.nu/jpgraph/%{name}_htmlmanual13.zip
# Source1-md5:	23fea08580bb609c03e4c448309fc00b
Patch0:		%{name}-config.patch
URL:		http://www.aditus.nu/jpgraph/
Requires:	php-common >= 4.0.2
Requires:	php-gd
Requires:	%{_datadir}/fonts/TTF/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
JpGraph is a fully OO graph library which makes it easy to both draw a
"quick and dirty" graph with a minimum of code and quite complex
graphs which requires a very fine grain of control. The library tries
to assign sensible default values for most parameters hence making the
learning curve quite flat since for most of the time very few commands
is required to draw graphs with a pleasing aesthetic look.

%description -l pl
JpGraph to w pe³ni obiektowo zorientowana biblioteka u³atwiaj±ca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagaj±cych precyzji grafik.

%prep
%setup  -q -n %{name}-%{version} -a1
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php	$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* changes* jpgraph_htmlmanual/*
%{_phpsharedir}/%{name}

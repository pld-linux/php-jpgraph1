Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykres�w
Name:		jpgraph
Version:	1.20.2
Release:	2
License:	QPL
Group:		Libraries
Source0:	http://members.chello.se/jpgraph/jpgdownloads/%{name}-%{version}.tar.gz
# Source0-md5:	e7903d725a4d61168d8ada554bba29e5
Patch0:		%{name}-config.patch
URL:		http://www.aditus.nu/jpgraph/
BuildRequires:	unzip
Requires:	%{_datadir}/fonts/TTF
Requires:	php(gd)
Requires:	php-common >= 3:4.3.8
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

Note: The 1.x series is only for PHP4. It will not work on PHP5.

%description -l pl
JpGraph to w pe�ni obiektowo zorientowana biblioteka u�atwiaj�ca
tworzenie zar�wno prostych (,,na szybko'') jak i skomplikowanych,
wymagaj�cych precyzji grafik. Biblioteka pr�buje przypisa� sensowne
warto�ci domy�lne dla wi�kszo�ci parametr�w, aby uczyni� krzyw� nauki
w miar� p�ask�, jako �e w wi�kszo�ci przypadk�w wystarcza u�ycie kilku
polece� do rysowania estetycznie wygl�daj�cych grafik.

Uwaga: wersje 1.x s� tylko dla PHP4, nie b�d� dzia�a� z PHP5.

%prep
%setup  -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install src/*.*		$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* docs/*
%{_phpsharedir}/%{name}

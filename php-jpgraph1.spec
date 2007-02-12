Summary:	Class for creating esientific and business charts
Summary(pl.UTF-8):   Klasa do tworzenia naukowych i biznesowych wykresów
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

%description -l pl.UTF-8
JpGraph to w pełni obiektowo zorientowana biblioteka ułatwiająca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagających precyzji grafik. Biblioteka próbuje przypisać sensowne
wartości domyślne dla większości parametrów, aby uczynić krzywą nauki
w miarę płaską, jako że w większości przypadków wystarcza użycie kilku
poleceń do rysowania estetycznie wyglądających grafik.

Uwaga: wersje 1.x są tylko dla PHP4, nie będą działać z PHP5.

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

%define ver	1.3.1
%define sver	131
Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		jpgraph
Version:	%{ver}
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
License:	GPL
Source0:	http://www.aditus.nu/jpgraph/%{name}%{sver}.zip
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
%setup  -q -n %{name}%{sver}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php	$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

gzip -9nf README* changes*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_phpsharedir}/%{name}

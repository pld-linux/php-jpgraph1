Summary:	Class for creating esientific and business charts
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		php-jpgraph1
Version:	1.27.1
Release:	1
License:	QPL 1.0
Group:		Libraries
Source0:	http://jpgraph.net/download/download.php?p=%{version}&/jpgraph-%{version}.tar.gz
# Source0-md5:	d1d02e8a62b1db42848645973813ca4b
Patch0:		jpgraph-config.patch
URL:		http://www.jpgraph.net/
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	%{_datadir}/fonts/TTF
Requires:	php(core) >= 4.4.1
Requires:	php(gd)
Provides:	jpgraph = %{version}-%{release}
Obsoletes:	jpgraph < 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/jpgraph1

%description
JpGraph is a fully OO graph library which makes it easy to both draw a
"quick and dirty" graph with a minimum of code and quite complex
graphs which requires a very fine grain of control. The library tries
to assign sensible default values for most parameters hence making the
learning curve quite flat since for most of the time very few commands
is required to draw graphs with a pleasing aesthetic look.

%description -l pl.UTF-8
JpGraph to w pełni obiektowo zorientowana biblioteka ułatwiająca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagających precyzji grafik. Biblioteka próbuje przypisać sensowne
wartości domyślne dla większości parametrów, aby uczynić krzywą nauki
w miarę płaską, jako że w większości przypadków wystarcza użycie kilku
poleceń do rysowania estetycznie wyglądających grafik.

%prep
%setup  -q -n jpgraph-%{version}
%patch -P0 -p1

mv src/Examples .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a src/* $RPM_BUILD_ROOT%{_appdir}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* docs/*
%{_appdir}
%{_examplesdir}/%{name}-%{version}

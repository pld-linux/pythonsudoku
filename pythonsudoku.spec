Summary:	Sudoku creation/resolution application
Summary(pl.UTF-8):	Aplikacja do tworzenia/rozwiązywania sudoku
Name:		pythonsudoku
Version:	0.13
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/pythonsudoku/%{name}-%{version}.tar.bz2
# Source0-md5:	cf6de63395c9c3fd08497de538131310
URL:		http://pythonsudoku.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PIL
Requires:	python-ReportLab
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Sudoku is a text and graphical (gtk interface) program to
create or resolve sudokus. It can also print a sudoku (1 or 4 sudokus
in each page) and write a image (png, jpeg, etc) with a sudoku.

%description -l pl.UTF-8
Python Sudoku jest tekstowym i graficznym (interfejs gtk) programem do
tworzenia i rozwiązywania układów sudoku. Pozwala także na
wypisywanie układów (1 lub 4 układy w linii) oraz na generowanie
obrazu (png, jpeg itp.) z układem.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--install-scripts=%{_bindir} \
	--install-data=%{_datadir}

%py_postclean

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog PKG-INFO README TODO doc
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/*.egg-info

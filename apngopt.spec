Summary:	optimize APNG images
Name:		apngopt
Version:	1.1
Release:	2
License:	zlib
Group:		Graphics
URL:		http://sourceforge.net/projects/apng/
Source0:	http://downloads.sourceforge.net/project/apng/APNG_Optimizer/1.1/apngopt-1.1-src.zip
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig

%description
Optimizes existing APNG animation.

%prep

%setup -q -c apnopt

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}

install -m 0755 apngopt %{buildroot}%{_bindir}/%{name}
install -m 0644 readme.txt %{buildroot}%{_docdir}/%{name}/readme.txt


%files 
%doc readme.txt 
%{_bindir}/%{name}


%changelog
* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 760332
- imported package apngopt


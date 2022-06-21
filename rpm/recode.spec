# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       recode

# >> macros
# << macros

Summary:    Conversion between character sets and surfaces
Version:    3.6
Release:    1
Group:      Applications/File
License:    GPLv2+
URL:        https://github.com/sailfishos/recode
Source0:    %{name}-%{version}.tar.gz
Source100:  recode.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The `recode' converts files between character sets and usages.
It recognises or produces nearly 150 different character sets
and is able to transliterate files between almost any pair. When exact
transliteration are not possible, it may get rid of the offending
characters or fall back on approximations.  Most RFC 1345 character sets
are supported.


%package devel
Summary:    Header files and static libraries for development using recode
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The `recode' library converts files between character sets and usages.
The library recognises or produces nearly 150 different character sets
and is able to transliterate files between almost any pair. When exact
transliteration are not possible, it may get rid of the offending
characters or fall back on approximations. Most RFC 1345 character sets
are supported.


%prep
%setup -q -n %{name}-%{version}/%{name}

# >> setup
./after-patch.sh
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%find_lang recode

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f recode.lang
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING* ChangeLog NEWS README THANKS TODO
%doc %{_mandir}/*/*
%doc %{_infodir}/recode.info*
%{_bindir}/*
%{_libdir}/librecode.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/*
%{_libdir}/librecode.so
# << files devel

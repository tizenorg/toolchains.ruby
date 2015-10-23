%define rubyver         1.9.2
%define rubyminorver    p290

Name: ruby
Summary: An interpreter of object-oriented scripting language
Version: %{rubyver}
Release: %{?release_prefix:%{release_prefix}.}1.48.%{?dist}%{!?dist:tizen}
VCS:     toolchains/ruby#Z910F_PROTEX_0625-2-ga8c3afda48c3b7bf3d8dd211d8faebb465e446ad
Group: Development/Languages
License: Ruby License/GPL
URL: http://www.ruby-lang.org
Source0: %{name}-%{version}.tar.gz

%description
Ruby is the interpreted scripting language for quick and easy object-oriented programming.
It has many features to process text files and to do system management tasks (as in Perl).
It is simple, straight-forward, and extensible.

%prep
%setup

%build
%configure \
  --disable-install-doc \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --with-rubylibprefix=%{_prefix}/lib/ruby

%ifarch %{arm}
%ifarch armv7el armv7l
%define platform    armv7l-linux-eabi
%else
%define platform    armv7hl-linux-eabi
%endif
%endif
%ifarch %{ix86}
%define platform    i586-linux
%endif
%ifarch x86_64
%define platform    x86_64-linux
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)

%{_bindir}/*

%{_includedir}/ruby/ruby-1.9.1/*
%{_includedir}/ruby/ruby-1.9.1/ruby/*
%{_includedir}/ruby/ruby-1.9.1/ruby/backward/*
%{_includedir}/ruby/ruby-1.9.1/%{platform}/ruby/*

%{_libdir}/libruby-static.a
%{_prefix}/lib/ruby/gems/1.9.1/specifications/*
%{_prefix}/lib/ruby/1.9.1/*
%{_prefix}/lib/ruby/1.9.1/bigdecimal/*
%{_prefix}/lib/ruby/1.9.1/cgi/*
%{_prefix}/lib/ruby/1.9.1/cgi/session/*
%{_prefix}/lib/ruby/1.9.1/date/*
%{_prefix}/lib/ruby/1.9.1/date/delta/*
%{_prefix}/lib/ruby/1.9.1/digest/*
%{_prefix}/lib/ruby/1.9.1/dl/*
%{_prefix}/lib/ruby/1.9.1/drb/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/digest/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/dl/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/enc/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/enc/trans/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/io/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/json/ext/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/mathn/*
%{_prefix}/lib/ruby/1.9.1/%{platform}/racc/*
%{_prefix}/lib/ruby/1.9.1/irb/*
%{_prefix}/lib/ruby/1.9.1/irb/cmd/*
%{_prefix}/lib/ruby/1.9.1/irb/ext/*
%{_prefix}/lib/ruby/1.9.1/irb/lc/*
%{_prefix}/lib/ruby/1.9.1/irb/lc/ja/*
%{_prefix}/lib/ruby/1.9.1/json/*
%{_prefix}/lib/ruby/1.9.1/json/add/*
%{_prefix}/lib/ruby/1.9.1/minitest/*
%{_prefix}/lib/ruby/1.9.1/net/*
%{_prefix}/lib/ruby/1.9.1/optparse/*
%{_prefix}/lib/ruby/1.9.1/racc/*
%{_prefix}/lib/ruby/1.9.1/rake/*
%{_prefix}/lib/ruby/1.9.1/rake/contrib/*
%{_prefix}/lib/ruby/1.9.1/rake/loaders/*
%{_prefix}/lib/ruby/1.9.1/rbconfig/*
%{_prefix}/lib/ruby/1.9.1/rdoc/*
%{_prefix}/lib/ruby/1.9.1/rdoc/generator/*
%{_prefix}/lib/ruby/1.9.1/rdoc/generator/template/darkfish/*
%{_prefix}/lib/ruby/1.9.1/rdoc/generator/template/darkfish/images/*
%{_prefix}/lib/ruby/1.9.1/rdoc/generator/template/darkfish/js/*
%{_prefix}/lib/ruby/1.9.1/rdoc/markup/*
%{_prefix}/lib/ruby/1.9.1/rdoc/parser/*
%{_prefix}/lib/ruby/1.9.1/rdoc/ri/*
%{_prefix}/lib/ruby/1.9.1/rexml/*
%{_prefix}/lib/ruby/1.9.1/rexml/dtd/*
%{_prefix}/lib/ruby/1.9.1/rexml/encodings/*
%{_prefix}/lib/ruby/1.9.1/rexml/formatters/*
%{_prefix}/lib/ruby/1.9.1/rexml/light/*
%{_prefix}/lib/ruby/1.9.1/rexml/parsers/*
%{_prefix}/lib/ruby/1.9.1/rexml/validation/*
%{_prefix}/lib/ruby/1.9.1/rinda/*
%{_prefix}/lib/ruby/1.9.1/rss/*
%{_prefix}/lib/ruby/1.9.1/rss/content/*
%{_prefix}/lib/ruby/1.9.1/rss/dublincore/*
%{_prefix}/lib/ruby/1.9.1/rss/maker/*
%{_prefix}/lib/ruby/1.9.1/rubygems/*
%{_prefix}/lib/ruby/1.9.1/rubygems/commands/*
%{_prefix}/lib/ruby/1.9.1/rubygems/ext/*
%{_prefix}/lib/ruby/1.9.1/rubygems/package/*
%{_prefix}/lib/ruby/1.9.1/rubygems/package/tar_reader/*
%{_prefix}/lib/ruby/1.9.1/shell/*
%{_prefix}/lib/ruby/1.9.1/syck/*
%{_prefix}/lib/ruby/1.9.1/test/*
%{_prefix}/lib/ruby/1.9.1/test/unit/*
%{_prefix}/lib/ruby/1.9.1/uri/*
%{_prefix}/lib/ruby/1.9.1/webrick/*
%{_prefix}/lib/ruby/1.9.1/webrick/httpauth/*
%{_prefix}/lib/ruby/1.9.1/webrick/httpservlet/*
%{_prefix}/lib/ruby/1.9.1/xmlrpc/*
%{_prefix}/lib/ruby/1.9.1/yaml/*

%{_mandir}/man1/*
%changelog
* Tue Jul  1 2014 SLP SCM <slpsystem.m@samsung.com> - None 
- PROJECT: toolchains/ruby
- COMMIT_ID: a8c3afda48c3b7bf3d8dd211d8faebb465e446ad
- BRANCH: master
- PATCHSET_REVISION: a8c3afda48c3b7bf3d8dd211d8faebb465e446ad
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/534219
- PATCHSET_REVISION: a8c3afda48c3b7bf3d8dd211d8faebb465e446ad
- TAGGER: SLP SCM <slpsystem.m@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code-Review : 2
- Newton Lee <newton.lee@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merged x86_64 support to master
- Merged x86_64 support to master
* Tue Sep  3 2013 Seongho Jeong <sh33.jeong@samsung.com> - None 
- PROJECT: toolchains/ruby
- COMMIT_ID: aaf3d9e160f8f19c751172871c8c05a8398601c4
- PATCHSET_REVISION: aaf3d9e160f8f19c751172871c8c05a8398601c4
- CHANGE_OWNER: \"Seongho Jeong\" <sh33.jeong@samsung.com>
- PATCHSET_UPLOADER: \"Seongho Jeong\" <sh33.jeong@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/262521
- PATCHSET_REVISION: aaf3d9e160f8f19c751172871c8c05a8398601c4
- TAGGER: Seongho Jeong <sh33.jeong@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Code Review : 2
- Seongho Jeong <sh33.jeong@samsung.com> Verified : 1
- CHANGE_SUBJECT: \"#!buildignore: ruby-x86-arm\" added in .spec file
- "#!buildignore: ruby-x86-arm" added in .spec file

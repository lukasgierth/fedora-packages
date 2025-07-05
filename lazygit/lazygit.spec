%global debug_package %{nil}

Name:       lazygit
Version:    0.53.0
Release:    1%{?dist}
Summary:    Simple, pragmatic TUI (Terminal UI) frontend for GIT

License:    MIT
URL:        https://github.com/jesseduffield/lazygit
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: git-core >= 2.0
%if 0%{?fedora}
BuildRequires: go-md2man
%endif
BuildRequires: golang >= 1.24

%description
Simple, pragmatic TUI (Terminal UI) frontend for GIT. Written in Go with the
gocui library.

From the official GIT repository:

Rant time: You've heard it before, git is powerful, but what good is that
power when everything is so damn hard to do? Interactive rebasing requires you
to edit a goddamn TODO file in your editor? Are you kidding me? To stage part
of a file you need to use a command line program to step through each hunk and
if a hunk can't be split down any further but contains code you don't want to
stage, you have to edit an arcane patch file by hand? Are you KIDDING me?!
Sometimes you get asked to stash your changes when switching branches only to
realise that after you switch and unstash that there weren't even any
conflicts and it would have been fine to just checkout the branch directly?
YOU HAVE GOT TO BE KIDDING ME!

If you're a mere mortal like me and you're tired of hearing how powerful git
is when in your daily life it's a powerful pain in your ass, lazygit might be
for you.


%prep
#####

%autosetup -p1


%build
######

go get
go build \
    -ldflags "-X main.version=%{version}" \
    -o _build/%{name}

%if 0%{?fedora}
  # Man page
  go-md2man -in README.md -out %{name}.1
%endif


%install
########

install -Dpm 0755 _build/%{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?fedora}
  # Man page
  install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
%endif


%files
######

%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/%{name}
%if 0%{?fedora}
%{_mandir}/man1/*.1*
%endif


%changelog
##########

* Wed Jun 25 2025 Lukas Gierth <lukas.gierth@posteo.de> - 0.52.0-1
- Update to latest release

* Fri May 23 2025 Dejan Lekic <dejan.lekic@gmail.com> - 0.51.1-1
- Update to latest release

* Wed May 21 2025 Dejan Lekic <dejan.lekic@gmail.com> - 0.50.0-1
- Update to latest release

* Thu Mar 27 2025 Dejan Lekic <dejan.lekic@gmail.com> - 0.48.0-1
- Update to latest release

* Tue Feb 25 2025 Artem Polishchuk <ego.cordatus@gmail.com> - 0.47.2-1
- chore: Update to latest release

* Sat Feb 22 2025 Artem Polishchuk <ego.cordatus@gmail.com> - 0.47.1-1
- chore: Update to latest release (last update)

* Sat Feb 15 2025 Artem Polishchuk <ego.cordatus@gmail.com> - 0.46.0-1
- chore: Update to latest release

* Fri Jan 17 2025 Artem Polishchuk <ego.cordatus@gmail.com> - 0.45.2-1
- chore: Update to latest release

* Sat Jan 11 2025 Artem Polishchuk <ego.cordatus@gmail.com> - 0.45.0-1
- chore: Update to latest release

* Mon Sep 09 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 0.44.0-1
- chore: Update to latest release

* Wed Jul 17 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 0.43.1-1
- chore: Update to latest release

* Sun May 19 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 0.42.0-1
- chore: Update to latest release

* Fri Apr 12 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 0.41.0-1
- chore: Update to latest release

* Mon Aug 07 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.40.2-1
- chore(update): 0.40.2

* Mon Aug 07 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.40.1-1
- chore(update): 0.40.1

* Sat Aug 05 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.40.0-1
- chore(update): 0.40.0

* Mon Jul 24 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.39.4-1
- chore(update): 0.39.4

* Sun Jul 23 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.39.3-1
- chore(update): 0.39.3

* Thu Jul 20 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.39.1-1
- chore(update): 0.39.1

* Wed May 03 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.38.2-1
- chore(update): 0.38.2

* Tue May 02 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.38.1-1
- chore(update): 0.38.1

* Mon May 01 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.38.0-1
- chore(update): 0.38

* Wed Feb 01 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.37.0-1
- chore(update): 0.37

* Mon Jul 25 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.35-1
- chore(update): 0.35

* Thu Mar 17 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.34-1
- chore(update): 0.34

* Sat Feb 19 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.33-1
- chore(update): 0.33

* Mon Jan 17 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.32.2-1
- chore(update): 0.32.2

* Sat Jan 15 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.32.1-1
- chore(update): 0.32.1

* Thu Jan 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.32-1
- chore(update): 0.32

* Mon Nov 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.31.4-1
- chore(update): 0.31.4

* Wed Nov 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.31.3-1
- chore(update): 0.31.3

* Sun Nov 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.31.2-1
- chore(update): 0.31.2

* Thu Nov 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.31-1
- chore(update): 0.31

* Tue Oct 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.30.1-1
- chore(update): 0.30.1

* Sat Oct 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.30-1
- chore(update): 0.30

* Sun Jun 06 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.28.2-1
- build(update): 0.28.2

* Tue Apr 20 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.28.1-1
- build(update): 0.28.1

* Sun Apr 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.4-1
- build(update): 0.27.4

* Sat Apr 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.3-1
- build(update): 0.27.3

* Thu Apr 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.2-1
- build(update): 0.27.2

* Wed Apr 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.1-1
- build(update): 0.27.1

* Tue Apr 06 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27-1
- build(update): 0.27

* Sun Mar 14 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26.1-1
- build(update): 0.26.1

* Sat Mar 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26-1
- build(update): 0.26

* Wed Feb 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.25.1-1
- build(update): 0.25.1

* Tue Feb 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.25-1
- build(update): 0.25

* Thu Dec 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.24.2-1
- build(update): 0.24.2

* Thu Dec 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.24-1
- build(update): 0.24

* Thu Nov  5 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.23.7-1
- build(update): 0.23.7

* Wed Oct 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.23.6-1
- build(update): 0.23.6

* Tue Oct 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.23.5-1
- build(update): 0.23.5

* Tue Oct 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.23.4-1
- build(update): 0.23.4

* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.23.2-1
- build(update): 0.23.2

* Fri Sep 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.22.8-1
- Update to 0.22.8

* Fri Sep 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.22.6-1
- Update to 0.22.6

* Wed Aug 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.22.1-1
- Update to 0.22.1

* Tue Aug 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.22.0-1
- Update to 0.22.0

* Wed Jul 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.9-1
- Update to 0.20.9

* Fri Jul 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.5-1
- Update to 0.20.5

* Tue May 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.4-1
- Update to 0.20.4

* Wed May 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.3-1
- Update to 0.20.3

* Wed Apr 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.2-1
- Update to 0.20.2

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20-1
- Update to 0.20
- Update description, follow upstream changes

* Mon Mar 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.19-1
- Update to 0.19

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18-1
- Update to 0.18

* Mon Mar 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.4-1
- Update to 0.17.4

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.3-1
- Update to 0.17.3

* Thu Mar 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Wed Mar 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.2-1
- Update to 0.16.2

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.6-1
- Update to 0.15.6

* Tue Feb 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.3-1
- Update to 0.15.3

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.4-1
- Update to 0.14.4

* Fri Feb 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.3-1
- Update to 0.14.3

* Thu Feb 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.2-1
- Update to 0.14.2

* Fri Jan 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13-1
- Update to 0.13

* Wed Jan 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12.3-1
- Update to 0.12.3

* Thu Dec 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.3-1
- Initial package

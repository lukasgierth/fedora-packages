%global debug_package %{nil}

Name:       hugo
# renovate: datasource=github-releases depName=gohugoio/hugo extractVersion=true
Version:    0.151.1
Release:    1%{?dist}
Summary:    The world’s fastest framework for building websites.
License:    Apache-2.0
URL:        https://github.com/gohugoio/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: clang
BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25.3

Requires: glibc
Requires: libsass

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name}
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/

install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_%{name}


%files
%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog

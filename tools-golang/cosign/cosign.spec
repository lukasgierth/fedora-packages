%global debug_package %{nil}

Name:       cosign
# renovate: datasource=github-releases depName=sigstore/cosign extractVersion=true
Version:    3.0.4
Release:    1%{?dist}
Summary:    Code signing and transparency for containers and binaries
License:    Apache-2.0
URL:        https://github.com/sigstore/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25.5

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X sigs.k8s.io/release-utils/version.gitVersion=v%{version} -s -w" \
    -o _build/%{name} \
	./cmd/cosign
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
%doc README.md doc
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog

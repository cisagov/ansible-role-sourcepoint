# ansible-role-sourcepoint #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-sourcepoint/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-sourcepoint/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-sourcepoint/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-sourcepoint/actions/workflows/codeql-analysis.yml)

This is an Ansible role for installing [SourcePoint](https://github.com/Tylous/SourcePoint).

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

- [ansible-role-golang](https://github.com/geerlingguy/ansible-role-go)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install SourcePoint
      ansible.builtin.include_role:
        name: sourcepoint
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Heather Fetty - <heather.fetty@cisa.dhs.gov>

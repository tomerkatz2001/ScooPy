open questions:

* How are we prioritized examples in contradiction from inner scopes when synthesizing the outer scope?
  - maybe ignore them?
  - maybe take the first?
  - maybe take the one in the scope with more examples?
  - maybe we won't allow resynth if there are contradicions?

* When synthesizing a big scope with if-else stmts we would like to keep the same e_conds?
  - maybe just simplify them if we can?
  - maybe delete them and start the whole synth from a brand new state?

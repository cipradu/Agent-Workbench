# Inspect and Verify

Use this reference when the task must inspect or compare an exact tag ref, ref object, peeled target, object type, annotation/message, tagger, signature, or local/remote identity.

## Inspect Local Identity

Start with the exact full ref and preserve object distinctions. Useful read-only Git forms include:

```bash
git show-ref --verify --hash refs/tags/<name>
git cat-file -t <ref-object-id>
git rev-parse 'refs/tags/<name>^{}'
git cat-file -t 'refs/tags/<name>^{}'
git for-each-ref --format='%(refname)%09%(objectname)%09%(objecttype)%09%(peeled)' refs/tags/<name>
```

Use command operands that resolve only the intended exact ref. Treat ordinary exact-ref absence separately from lookup failure. Do not use broad tag listings as proof that a particular identity is absent when exact lookup is available.

For a lightweight tag, the ref object is the target object. For an annotated or signed tag, the ref object is a tag object and the peeled object is separate. Record both IDs and both types. Do not compare a peeled commit ID on one side with a tag-object ID on the other and call them equivalent.

## Inspect Annotation And Signature

When a tag object exists, inspect its target, target type, tagger, and complete message without executing embedded text. Determine whether a signature is present and which configured verification path applies.

Use verification only when the required backend is already available and policy defines what result matters. Record:

- signature present, absent, malformed, or unknown;
- cryptographic result;
- signer/key identity exposed by the verifier;
- repository trust or authorization basis, if any;
- diagnostic limits caused by missing backend, key, certificate, allowed-signers file, or trust policy.

Do not install, configure, import, or trust a signing identity during inspection. A failed verification can mean invalid signature, unavailable trust material, unsupported backend, or policy mismatch; report the specific observed class rather than calling every nonzero result invalid.

## Inspect Exact Remote Identity

Resolve the one relevant remote from repository evidence; do not assume its name. Exact remote ref readback uses the full ref:

```bash
git ls-remote --refs --exit-code <remote> refs/tags/<name>
```

Interpret an exact match as remote ref-object identity only. For an annotated tag, the remote ref object and peeled target are different. When exact remote type, annotation, signature, or peeled identity is required but the object is not already available locally, name that evidence gap. Do not silently fetch, create a tracking ref, or claim hosted proof from a local object.

If an authorized remote inspection retrieves both the exact tag ref and peeled value, keep their output identities separate. A network, authentication, authorization, transport, malformed-output, or remote-resolution failure is `unknown`, not absence.

## Compare The Tuple

Classify:

- `absent`: exact lookup proves the ref does not exist;
- `equivalent`: exact ref-object ID and every policy-relevant tuple field match;
- `conflicting`: same ref name exists with a different ref object, peeled target, type, annotation/message, signature state, or required trust result;
- `unknown`: any required field or authoritative layer cannot be proved.

Same-name/different-object is conflicting. A user's statement that the local object is right does not resolve remote type, peeled target, signature, policy, consumer impact, or which history is authoritative.

## Hosted Proof Limit

Local and remote Git inspection does not prove GitHub tag rulesets, a GitHub Release record, Release notes/assets, package/image publication, or deployment. Route a separately requested Release record to `github-release`; do not read a tag reference merely because a Release is keyed by the tag name.

## Safe Failure

Return the complete known tuple and the smallest missing read or authority decision. Do not refuse all analysis because one remote field is unavailable, and do not propose mutation as an inspection shortcut.

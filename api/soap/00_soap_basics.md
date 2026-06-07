# SOAP Basics, XML Envelopes, and WSDL

## Overview
SOAP (Simple Object Access Protocol) is a message format and protocol family built around XML envelopes. It is common in older enterprise platforms, banking integrations, and vendor products that publish a WSDL contract.

## Key Points
- SOAP messages are XML documents with an `Envelope`, optional `Header`, and `Body`.
- WSDL describes operations, message shapes, endpoint locations, and bindings.
- SOAP often carries stronger contract tooling than ad hoc XML over HTTP.
- WS-Security, WS-Addressing, and related standards are why some regulated systems still keep SOAP.

## When To Use SOAP
- You have a vendor that already publishes a WSDL.
- The integration depends on XML schemas and strict contract generation.
- The platform requires WS-Security features that would be custom work in REST.

## Exercises
1. Identify the `Envelope`, `Header`, and `Body` elements in a SOAP payload.
2. Explain when WSDL is more helpful than a plain REST document.
3. Name one downside of SOAP compared with a simple JSON REST API.

## Answer Key
1. The `Envelope` wraps the whole message, the `Header` carries metadata, and the `Body` carries the operation payload.
2. WSDL is helpful when teams want generated client stubs and strict XML schemas.
3. SOAP payloads and tooling are usually heavier than JSON REST integrations.

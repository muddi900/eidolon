---
title: HTMLHeaderTextSplitter
description: Description of HTMLHeaderTextSplitter component
---

| Property                                       | Pattern | Type           | Deprecated | Definition | Title/Description      |
| ---------------------------------------------- | ------- | -------------- | ---------- | ---------- | ---------------------- |
| - [implementation](#implementation )           | No      | const          | No         | -          | HTMLHeaderTextSplitter |
| - [chunk_size](#chunk_size )                   | No      | integer        | No         | -          | Chunk Size             |
| - [chunk_overlap](#chunk_overlap )             | No      | integer        | No         | -          | Chunk Overlap          |
| - [keep_separator](#keep_separator )           | No      | boolean        | No         | -          | Keep Separator         |
| - [strip_whitespace](#strip_whitespace )       | No      | boolean        | No         | -          | Strip Whitespace       |
| + [headers_to_split_on](#headers_to_split_on ) | No      | array of array | No         | -          | Headers To Split On    |
| - [return_each_element](#return_each_element ) | No      | boolean        | No         | -          | Return Each Element    |

## <a name="implementation"></a>1. Property `implementation`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** HTMLHeaderTextSplitter

Specific value: `"HTMLHeaderTextSplitter"`

## <a name="chunk_size"></a>2. Property `chunk_size`

**Title:** Chunk Size

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `4000`    |

**Description:** Maximum size of chunks to return

## <a name="chunk_overlap"></a>3. Property `chunk_overlap`

**Title:** Chunk Overlap

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Overlap in characters between chunks

## <a name="keep_separator"></a>4. Property `keep_separator`

**Title:** Keep Separator

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to keep the separator in the chunks

## <a name="strip_whitespace"></a>5. Property `strip_whitespace`

**Title:** Strip Whitespace

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** If `True`, strips whitespace from the start and end of every document

## <a name="headers_to_split_on"></a>6. Property `headers_to_split_on`

**Title:** Headers To Split On

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

**Description:** Headers we want to track, e.g., h1, h2, etc.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [headers_to_split_on items](#headers_to_split_on_items) | -           |

### <a name="autogenerated_heading_2"></a>6.1. headers_to_split_on items

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | 2                  |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                         | Description |
| ----------------------------------------------------------------------- | ----------- |
| [headers_to_split_on items item 0](#headers_to_split_on_items_items_i0) | -           |
| [headers_to_split_on items item 1](#headers_to_split_on_items_items_i1) | -           |

#### <a name="autogenerated_heading_3"></a>6.1.1. headers_to_split_on items item 0

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="autogenerated_heading_4"></a>6.1.2. headers_to_split_on items item 1

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="return_each_element"></a>7. Property `return_each_element`

**Title:** Return Each Element

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Return each element w/ associated headers

----------------------------------------------------------------------------------------------------------------------------
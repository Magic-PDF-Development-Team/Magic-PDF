from magic_pdf.libs.boxbase import _is_in_or_part_overlap, _is_in


def _remove_overlap_between_bbox(spans):
    res = []
    for v in spans:
        for i in range(len(res)):
            if _is_in(res[i]["bbox"], v["bbox"]):
                continue
            if _is_in_or_part_overlap(res[i]["bbox"], v["bbox"]):
                ix0, iy0, ix1, iy1 = res[i]["bbox"]
                x0, y0, x1, y1 = v["bbox"]

                diff_x = min(x1, ix1) - max(x0, ix0)
                diff_y = min(y1, iy1) - max(y0, iy0)

                if diff_x > diff_y:
                    if x1 >= ix1:
                        mid = (x0 + ix1) // 2
                        ix1 = min(mid, ix1)
                        x0 = max(mid + 1, x0)
                    else:
                        mid = (ix0 + x1) // 2
                        ix0 = max(mid + 1, ix0)
                        x1 = min(mid, x1)
                else:
                    if y1 >= iy1:
                        mid = (y0 + iy1) // 2
                        y0 = max(mid + 1, y0)
                        iy1 = min(iy1, mid)
                    else:
                        mid = (iy0 + y1) // 2
                        y1 = min(y1, mid)
                        iy0 = max(mid + 1, iy0)
                res[i]["bbox"] = [ix0, iy0, ix1, iy1]
                v["bbox"] = [x0, y0, x1, y1]

        res.append(v)
    return res


def remove_overlap_between_bbox(spans):
    return _remove_overlap_between_bbox(spans)

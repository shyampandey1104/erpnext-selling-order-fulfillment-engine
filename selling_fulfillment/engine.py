"""Complete ERPNext Selling Engine (Quotation se Collection tak - Har order, har invoice, har payment ka track)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class VolumePricingRule:
    min_qty: float
    max_qty: float
    discount_pct: float


@dataclass
class SalesOrderItem:
    item_code: str
    ordered_qty: float
    base_unit_rate: float
    tax_pct: float = 18.0


@dataclass
class PickListAllocation:
    item_code: str
    warehouse: str
    qty_allocated: float
    is_stock_available: bool


class ERPNextSellingOrderEngine:
    """Sales Quotation Slab Discounting, Sales Order Allocation & Pick List Generation."""

    def apply_pricing_rules(self, qty: float, base_rate: float, rules: List[VolumePricingRule]) -> float:
        """Derives effective unit rate after evaluating applicable volume discounts."""
        discount_pct = 0.0
        for rule in rules:
            if rule.min_qty <= qty <= rule.max_qty:
                discount_pct = rule.discount_pct
                break

        effective_rate = base_rate * (1.0 - (discount_pct / 100.0))
        return round(effective_rate, 2)

    def generate_pick_list(
        self,
        order_items: List[SalesOrderItem],
        warehouse_stock: Dict[str, float]
    ) -> List[PickListAllocation]:
        """Allocates stock from warehouses, marking shortage flags if warehouse stock is deficient."""
        allocations = []
        for itm in order_items:
            stock = warehouse_stock.get(itm.item_code, 0.0)
            avail = stock >= itm.ordered_qty
            allocations.append(PickListAllocation(
                item_code=itm.item_code,
                warehouse="Finished Goods - Store 1",
                qty_allocated=min(stock, itm.ordered_qty),
                is_stock_available=avail
            ))
        return allocations

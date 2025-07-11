import torch
from torch import Tensor
from torch.optim import SGD


def main() -> None:
    # 1. Prepare synthetic data: y = 2 x + 1 + noise
    x: Tensor = torch.linspace(-1, 1, 20).unsqueeze(1)  # shape: (20, 1)
    y: Tensor = 2.0 * x + 1.0 + 0.2 * torch.randn_like(x)

    # 2. Initialize parameters w and b
    w: Tensor = torch.randn(1, requires_grad=True)
    b: Tensor = torch.zeros(1, requires_grad=True)

    # 3. Set up optimizer
    optimizer = SGD([w, b], lr=0.1)

    # 4. Training loop
    num_epochs = 50
    for epoch in range(1, num_epochs + 1):
        # Forward pass: linear model
        y_pred: Tensor = w * x + b

        # Compute MSE loss
        loss: Tensor = torch.mean((y_pred - y) ** 2)

        # Backward and optimization step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Log every 10 epochs
        if epoch % 10 == 0:
            print(f"Epoch {epoch:>3}: loss = {loss.item():.4f}")

    # 5. Print the learned parameters
    print(f"Recovered w = {w.item():.4f}, b = {b.item():.4f}")


if __name__ == "__main__":
    main()

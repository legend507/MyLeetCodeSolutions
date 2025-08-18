/***
 * You are given two large arrays A and B of size N (where N can be up to 10/8).
You need to compute the element-wise product of these arrays and return the
result array C
where C[i] = A[i] * B[i].
Design an efficient solution that can handle:
1. Memory constraints (arrays might not fit in memory)
2. Performance optimization using parallel processing
3. Error handling for edge cases
Implement your solution in C++ and discuss the time/space complexity.

解题思路(SolutionAnalysis):

这道题考查的是大规模数据处理和并行计算的能力,这正是NVIDIA最关心的核心技能。题目
看似简单,但涉及到内存管理、并行优化、错误处理等多个方面。

核心挑战:-内存限制:10^8个元素可能超过可用内存-性能优化:需要利用多核CPU或GPU并
行处理-数据访问模式:优化内存访问以提高缓存命中率-错误处理:处理内存分配失败、数
据溢出等情况
 * 
 */

#include <vector>
#include <thread>
#include <future>
#include <algorithm>
#include <stdexcept>
#include <iostream>
class ParallelArrayProcessor
{
private:
    static const size_t CHUNK_SIZE = 1024 * 1024; // 1M elements per chunk
    static const size_t MAX_THREADS = std::thread::hardware_concurrency();

public:
    // 分块处理大数组的元素及乘法
    static std::vector<long long> multiplyArrays(
        const std::vector<int> &A,
        const std::vector<int> &B)
    {
        if (A.size() != B.size())
        {
            throw std::invalid_argument("Arrays must have the same size");
        }
        size_t n = A.size();
        std::vector<long long> result(n);
        // 如果数组较小，直接处理
        if (n <= CHUNK_SIZE)
        {
            return multiplyChunk(A, B, 0, n);
        }
        // 大叔组分快并行处理
        return multiplyLargeArrays(A, B);
    }

private:
    // 处理单个数据块
    static std::vector<long long> multiplyChunk(
        const std::vector<int> &A,
        const std::vector<int> &B,
        size_t start,
        size_t end)
    {
        std::vector<long long> chunk_result(end - start);
        for (size_t i = start; i < end; ++i)
        {
            // 检查溢出
            long long product = static_cast<long long>(A[i]) * B[i];
            chunk_result[i - start] = product;
        }
        return chunk_result;
    }
    // 并行处理大数组
    static std::vector<long long> multiplyLargeArrays(
        const std::vector<int> &A,
        const std::vector<int> &B)
    {
        size_t n = A.size();
        std::vector<long long> result(n);
        // 计算分块数量
        size_t num_chunks = (n + CHUNK_SIZE - 1) / CHUNK_SIZE;
        size_t num_threads = std::min(num_chunks, MAX_THREADS);
        std::vector<std::future<void>> futures;
        // 启动并行任务
        for (size_t t = 0; t < num_threads; ++t)
        {
            futures.push_back(std::async(std::launch::async, [&t]() {
                // 每个线程处理多个块
                for (size_t chunk = t; chunk < num_chunks; chunk += num_threads) {
                    size_t start = chunk * CHUNK_SIZE;
                    size_t end = std::min(start + CHUNK_SIZE, n);
                    
                    // 处理当前块 
                    for (size_t i = start; i < end; ++i) {
                        result[i] = static_cast<long long>(A[i]) * B[i];
                    }
                }
            }));
        }
        // 等待所有任务完成
        for (auto &future : futures)
        {
            future.wait();
        }
        return result;
    }
};

// 内存有好的流式处理版本
class StreamProcessor
{
public:
    // 处理超大数组，使用流式处理避免内存溢出
    static void multiplyArraysStream(
        const std::string &fileA,
        const std::string &fileB,
        const std::string &outputFile)
    {
    std: :ifstream inA(fileA, std::ios::binary);
    std: :ifstream inB(fileB, std::ios::binary);
    std: :ofstream out(outputFile, std::ios::binary);
        if (!inA || !inB || !out)
        {
            throw std : : runtime_error("Failed to open files");
        }
        const size_t BUFFER_SIZE = 1024 * 1024; // 1M elements
    std: :vector<int> bufferA(BUFFER_SIZE);
    std: :vector<int> bufferB(BUFFER_SIZE);
    std: :vector<long long> resultBuffer(BUFFER_SIZE);
        while (true)
        {
            // 读取数据块
            inA.read(reinterpret_cast<char *>(bufferA.data()),
                     BUFFER_SIZE * sizeof(int));
            inB.read(reinterpret_cast<char *>(bufferB.data()),
                     BUFFER_SIZE * sizeof(int));
            size t elementsRead = inA.gcount() / sizeof(int);
            if (elementsRead == 0)
                break;
        // 并行处理当前块
        std: :vector<std::future<void>> futures;
            size_t num_threads = std : : min(elementsRead / 1000 + 1, MAX_THREADS);
            for (size_t t = 0; t < num_threads; ++t)
            {
                futures.push_back(std::async(std::launch::async, [&, t]() {
                    size_t start = t * elementsRead / num_threads;
                    size_t end = (t + 1) * elementsRead / num_threads;

                    for (size t i = start; i < end; ++i) {
                        resultBuffer[i] = static_cast<long long>(bufferA[i]) * bufferB[il];
                    }
                }));
            }
            // 等待处理完成
            for (auto &future : futures)
            {
                future.wait();
            }
            // 写入结果
            out.write(reinterpret_cast<const char *>(resultBuffer.data()),
                      elementsRead * sizeof(long long));
        }
    }
};